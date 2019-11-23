#!/usr/bin/env python

from pypifi.pipeline import Pipeline

from filters.meta_data_filter import MetaDataFilter

from filters.user_data_filter import UserDataFilter
from filters.authorization_data_filter import AuthorizationDataFilter
from filters.mutate_data_filter import MutateDataFilter

from messages.meta_data_message import MetaDataMessage

from messages.user_data_message import UserDataMessage

from messages.mutate_data_message import MutateDataMessage

def test1():
    print('--- starting test1:')
    pipe = Pipeline()
    pipe.connect(MetaDataFilter())
    pipe.execute(MetaDataMessage('lumannnn', 'a simple test message'))
    print('--- finished test1')

def test2():
    print('--- starting test2:')
    pipe = Pipeline()
    pipe.connect(UserDataFilter()).connect(AuthorizationDataFilter())
    pipe.execute(UserDataMessage('lumannnn', 'awesomely secure password'))
    print('--- finished test2')


def test3():
    print('--- starting test3:')
    pipe = Pipeline()
    pipe.connect(MutateDataFilter()) \
        .connect(MutateDataFilter()) \
        .connect(MutateDataFilter()) \
        .connect(MutateDataFilter())
    message = MutateDataMessage(1)
    mutated_message = pipe.execute(message)
    print(mutated_message.data)
    print('--- finished test3')


test3()
