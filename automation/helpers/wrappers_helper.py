import logging
from datetime import datetime
from filelock import FileLock

from automation.configurations.shared_consts import MINUTE
from automation.helpers.common_helper import convert_variable_to


class Retry(object):
    def __init__(self, exceptions_to_expect, retries=2, timeout=None):
        self.exceptions_to_expect = tuple(convert_variable_to(exceptions_to_expect))
        self.max_retries = retries
        self.timeout = timeout
        self.retry_method = self.retry_by_timeout if timeout is not None else self.retry_by_x_retries

    def __call__(self, func):
        def _retry(*args, **kwargs):
            func_tries = 0
            func_result = None
            exception = None
            start_time = datetime.now()
            method_running_time = (datetime.now() - start_time).seconds

            while self.retry_method(func_tries=func_tries,
                                    func_result=func_result,
                                    method_running_time=method_running_time):
                try:
                    func_result = func(*args, **kwargs)
                    return func_result
                except self.exceptions_to_expect as e:
                    exception = e
                finally:
                    func_tries += 1

            if exception is not None:
                raise exception

        return _retry

    def retry_by_x_retries(self, **kwargs):
        return kwargs.get('func_tries') < self.max_retries and kwargs.get('func_result') is None

    def retry_by_timeout(self, **kwargs):
        return kwargs.get('method_running_time') < self.timeout and kwargs.get('func_result') is None


class ElementFallback(object):
    def __call__(self, func):
        def _retry(*args, **kwargs):
            can_fallback = 'fallback_element' in kwargs and 'fallback_by' in kwargs

            try:
                result = func(*args, **kwargs)
                if can_fallback:
                    old_by = kwargs.pop('by') if 'by' in kwargs else args[1]
                    old_element = kwargs.pop('element') if 'element' in kwargs else args[2]
                    logging.warning("Fallback exists for the element but not used: 'by': %s, 'element': %s'" % (
                        old_by, old_element))
                return result

            except AssertionError as e:
                new_args = list(args)
                if can_fallback:
                    by = kwargs.pop('fallback_by')
                    element = kwargs.pop('fallback_element')
                    old_by = kwargs.pop('by') if 'by' in kwargs else new_args[1]
                    old_element = kwargs.pop('element') if 'element' in kwargs else new_args[2]

                    logging.error("USING OLD ELEMENTS!!!! \n"
                                  " OLD(fallback to): 'by': %s, 'element': %s'\n"
                                  " INSTEAD of new:   'by': %s, 'element': %s'" % (by, element, old_by, old_element))

                    if 'by' in kwargs:
                        kwargs['by'] = by
                    else:
                        new_args[1] = by

                    if 'element' in kwargs:
                        kwargs['element'] = element
                    else:
                        new_args[2] = element

                    return func(*new_args, **kwargs)
                else:
                    raise e

        return _retry


class MinLogLevel(object):
    def __init__(self, log_level=logging.INFO):
        self.tmp_log_level = log_level

    def __call__(self, func):
        def _method(*args, **kwargs):
            current_log_level = logging.getLogger().level
            logging.basicConfig(level=self.tmp_log_level)
            try:
                func_result = func(*args, **kwargs)
                return func_result
            finally:
                logging.basicConfig(level=logging.getLevelName(current_log_level))

        return _method


class ActionLock(object):
    def __init__(self, file_path, timeout=MINUTE):
        self.file_lock = FileLock(file_path, timeout=timeout)

    def __call__(self, func):
        def _method(*args, **kwargs):
            logging.getLogger("filelock").setLevel(logging.WARN)
            self.file_lock.acquire()

            try:
                func_result = func(*args, **kwargs)
                return func_result
            finally:
                self.file_lock.release()

        return _method


def timeit(method):
    def timed(*args, **kw):
        time_start = datetime.now()
        result = method(*args, **kw)
        time_diff = datetime.now() - time_start
        time_str = f"min:sec:micsec | " \
            f"{int(time_diff.seconds / MINUTE)}:{time_diff.seconds % MINUTE}:{str(time_diff.microseconds)[:3]}"
        logging.info(f"[[ Method Duration]] `{method.__name__}` -> {time_str}")
        return result

    return timed
