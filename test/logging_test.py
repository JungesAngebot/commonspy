import unittest

from commonspy.logging import build_message_from_exception_chain


class BuildMessageFromExceptionChainTest(unittest.TestCase):
    def test_single_exception(self):
        message = ''
        try:
            generate_exception_one()
        except Exception as e:
            message = build_message_from_exception_chain(e)
        self.assertEquals("one", message)

    def test_two_exceptions(self):
        message = ''
        try:
            chain_exception_two()
        except Exception as e:
            message = build_message_from_exception_chain(e)
        self.assertEquals("two | one", message)

    def test_three_exceptions(self):
        message = ''
        try:
            chain_exception_three()
        except Exception as e:
            message = build_message_from_exception_chain(e)
        self.assertEquals("three | two | one", message)


def generate_exception_one():
    raise Exception("one")


def chain_exception_two():
    try:
        generate_exception_one()
    except Exception as e:
        raise Exception("two") from e


def chain_exception_three():
    try:
        chain_exception_two()
    except Exception as e:
        raise Exception("three") from e
