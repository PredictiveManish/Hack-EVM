"""
Tests for package imports and module structure.

Ensures that all modules can be imported correctly
and that the package metadata is properly configured.
"""

import importlib


class TestImports:
    """Test package importability."""

    def test_import_package(self) -> None:
        """Test that the main package can be imported."""
        hack_evm = importlib.import_module("hack_evm")
        assert hack_evm is not None

    def test_import_core(self) -> None:
        """Test that core module can be imported."""
        core = importlib.import_module("hack_evm.core")
        assert core is not None

    def test_import_cli(self) -> None:
        """Test that CLI module can be imported."""
        cli = importlib.import_module("hack_evm.cli")
        assert cli is not None

    def test_version_available(self) -> None:
        """Test that __version__ is defined."""
        hack_evm = importlib.import_module("hack_evm")
        assert hasattr(hack_evm, "__version__")
        assert hack_evm.__version__ == "0.1.0"

    def test_author_available(self) -> None:
        """Test that __author__ is defined."""
        hack_evm = importlib.import_module("hack_evm")
        assert hasattr(hack_evm, "__author__")
        assert "parody" in hack_evm.__author__.lower()

    def test_all_exports(self) -> None:
        """Test that __all__ contains expected functions."""
        hack_evm = importlib.import_module("hack_evm")
        assert hasattr(hack_evm, "__all__")
        assert "hack" in hack_evm.__all__
        assert "quantum_mode" in hack_evm.__all__
        assert "explain" in hack_evm.__all__

    def test_function_imports(self) -> None:
        """Test that functions can be imported from package."""
        from hack_evm import explain, hack, quantum_mode

        assert callable(hack)
        assert callable(quantum_mode)
        assert callable(explain)


class TestCoreFunctions:
    """Test core function signatures and type hints."""

    def test_hack_signature(self) -> None:
        """Test that hack function has proper signature."""
        from hack_evm import hack

        assert callable(hack)
        # Test with default argument
        result = hack()
        assert isinstance(result, dict)

    def test_quantum_mode_signature(self) -> None:
        """Test quantum_mode function signature."""
        from hack_evm import quantum_mode

        assert callable(quantum_mode)
        result = quantum_mode()
        assert isinstance(result, dict)

    def test_explain_signature(self) -> None:
        """Test explain function signature."""
        from hack_evm import explain

        assert callable(explain)
        result = explain()
        assert isinstance(result, str)


class TestPackageMetadata:
    """Test package metadata."""

    def test_package_name(self) -> None:
        """Test package name."""
        hack_evm = importlib.import_module("hack_evm")
        assert hack_evm.__name__ == "hack_evm"

    def test_module_docstring(self) -> None:
        """Test that package has docstring."""
        hack_evm = importlib.import_module("hack_evm")
        assert hack_evm.__doc__ is not None
        assert "SATIRE" in hack_evm.__doc__.upper() or "parody" in hack_evm.__doc__.lower()
