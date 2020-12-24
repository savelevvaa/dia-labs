import pytest
from pytest import fixture
from pytest_bdd import *
import StatePattern

@pytest.fixture
def computer():
    return StatePattern.Computer()


@scenario('state.feature', 'On the computer')
def test_On_computer():
    pass

@given("Computer is Off")
def comuterIsOff(computer):
    computer.state.name == "off"

@when("Switching on")
def switchingOn(computer):
    computer.change(StatePattern.On)

@then("State should be On")
def no_error_message(computer):
    assert computer.state.name == "on"

@scenario('state.feature', 'Suspend the computer')
def test_Suspend_computer():
    pass

@given("Computer is On")
def comuterIsOff(computer):
    computer.state.name == "on"

@when("Switching Suspend")
def switchingOn(computer):
    computer.change(StatePattern.On)
    computer.change(StatePattern.Suspend)

@then("State should be Suspend")
def no_error_message(computer):
    assert computer.state.name == "suspend"

@scenario('state.feature', 'Hibirnate the computer')
def test_Hibirnate_computer():
    pass

@given("Computer is Suspended")
def comuterIsOff(computer):
    computer.state.name == "on"

@when("Switching Hibirnate")
def switchingOn(computer):
    computer.change(StatePattern.On)
    computer.change(StatePattern.Suspend)
    computer.change(StatePattern.Hibernate)

@then("State should be Suspend")
def no_error_message(computer):
    assert computer.state.name == "suspend"