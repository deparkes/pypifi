#!/usr/bin/env python


class MutateDataFilter:

    def process(self, message):
        """
            message should be type of MutateDataMessage.
        """
        message.data += 1
