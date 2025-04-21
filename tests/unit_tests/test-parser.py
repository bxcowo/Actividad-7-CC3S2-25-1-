import pytest

from features.steps.belly_steps import step_when_wait_time_description
from src.belly import Belly

def test_parse_regex_validation():
    context = Belly()
    sentence = "Quince horas, 16 minutos y 200 segundos"
    step_when_wait_time_description(context, sentence)

    assert context.tiempo_esperado is not 0

def test_parse_regex_hours():
    context = Belly()
    sentence = "Veinte horas"
    step_when_wait_time_description(context, sentence)

    assert context.tiempo_esperado is 20

def test_parse_regex_huge_minutes():
    context = Belly()
    sentence = "8122039821 minutos"
    step_when_wait_time_description(context, sentence)

    assert context.tiempo_esperado is (8122039821/60)

def test_parse_regex_none_seconds():
    context = Belly()
    sentence = "cero segundos"
    step_when_wait_time_description(context, sentence)

    assert context.tiempo_esperado is 0

def test_parse_regex_minutes_seconds():
    context = Belly()
    sentence = "Cuarenta minutos y 13 segundos"
    step_when_wait_time_description(context, sentence)

    assert context.tiempo_esperado is ((40/60) + (13/3600))
