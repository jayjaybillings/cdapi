from fastapi import FastAPI
from fastapi.testclient import TestClient
from cdapi.CCLE_web_service import app

"""TestClient makes it possible to test the API."""
client = TestClient(app)

def test_read_main():
    """This tests the basic root path of the API."""
    response = client.get("/")
    assert response.status_code == 200

def test_check_hotspot():
    """This is a basic test of check_hotspot"""
    response = client.get("checkHotspot/?gene_id=7157&cell_line=ACH-000001")
    assert response.status_code == 200
    assert response.json() == True

def test_get_genes():
    """This is a basic test to make sure genes can be retrieved given
    a cell line."""
    genes = [7157, 7029, 5295, 107, 135941, 654463]
    response = client.get("genes/ACH-000001")
    assert response.status_code == 200
    assert response.json() == genes

def test_get_cell_lines():
    """This is a basic test to make sure cell lines can be retrieved
    given a gene."""
    cell_lines = ['ACH-000450', 'ACH-000555', 'ACH-000835',
                      'ACH-000915', 'ACH-002097', 'ACH-002231',
                      'ACH-002309', 'ACH-002310', 'ACH-002338',
                      'ACH-002396', 'ACH-002510']
    response = client.get("cell_lines/259249")
    assert response.status_code == 200
    assert response.json() == cell_lines
