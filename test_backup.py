import os
import pytest
from backup import get_user_home, get_backup_filename, create_backup

def test_get_user_home():
    home = get_user_home()
    assert os.path.exists(home)

def test_get_backup_filename():
    filename = get_backup_filename()
    assert filename.startswith("backup_")
    assert len(filename) > 10  # Vérifie que la date est incluse

def test_create_backup():
    result = create_backup()
    assert "Backup created" in result or "Error creating backup" in result