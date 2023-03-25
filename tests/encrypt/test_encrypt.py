from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message('testando', 8) == 'odnatset'
    assert encrypt_message('testando', 4) == 'odna_tset'
    with pytest.raises(TypeError):
        encrypt_message('teste de função', '')
    with pytest.raises(TypeError):
        encrypt_message(1, 1)
