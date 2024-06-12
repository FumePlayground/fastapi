from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    
    schema = response.json()
    assert "paths" in schema, "Missing 'paths' in OpenAPI schema"
    assert "components" in schema, "Missing 'components' in OpenAPI schema"
    
    # Additional schema validations
    assert "info" in schema, "Missing 'info' in OpenAPI schema"
    assert "title" in schema["info"], "Missing 'title' in info section of OpenAPI schema"
    assert "version" in schema["info"], "Missing 'version' in info section of OpenAPI schema"
    
    assert "openapi" in schema, "Missing 'openapi' version in schema"
    assert schema["openapi"].startswith("3."), "OpenAPI version is not 3.x"

    # Ensure all paths have at least one method (GET, POST, etc.)
    for path, methods in schema["paths"].items():
        assert isinstance(methods, dict) and methods, f"No methods defined for path: {path}"
    
    # Check that components section defines "schemas" if any models are used
    if "schemas" in schema["components"]:
        assert isinstance(schema["components"]["schemas"], dict), "Schemas section is not a dictionary"
