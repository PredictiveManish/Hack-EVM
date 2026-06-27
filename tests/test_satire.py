"""
Tests specifically verifying the satirical nature of hack-evm.

Ensures that NO real hacking functionality exists in the package.
"""

import inspect


class TestNoRealHacking:
    """
    Verify that hack-evm contains absolutely NO real hacking capabilities.

    This test suite confirms the package is pure satire/parody.
    """

    def test_no_socket_imports(self) -> None:
        """Verify no socket/networking imports in core."""
        import hack_evm.core as core

        source = inspect.getsource(core)
        assert "import socket" not in source
        assert "import requests" not in source
        assert "import urllib" not in source
        assert "import paramiko" not in source
        assert "import subprocess" not in source
        assert "import os.system" not in source

    def test_no_file_operations(self) -> None:
        """Verify no file system operations."""
        import hack_evm.core as core

        source = inspect.getsource(core)
        assert "open(" not in source
        assert "os.remove" not in source
        assert "os.unlink" not in source
        assert "shutil" not in source

    def test_no_dynamic_code_execution(self) -> None:
        """Verify no dynamic code execution except for package version import."""
        import hack_evm.core as core

        source = inspect.getsource(core)
        # Only allow the __import__ for version checking
        source_without_version_check = source.replace('__import__("hack_evm")', "")
        assert "eval(" not in source_without_version_check
        assert "exec(" not in source_without_version_check

    def test_no_actual_exploits(self) -> None:
        """Verify no actual exploit code."""
        import hack_evm.core as core

        source = inspect.getsource(core)
        dangerous_keywords = [
            "overflow",
            "injection",
            "xss",
            "csrf",
            "payload",
            "shellcode",
            "ROP",
            "gadget",
        ]
        for keyword in dangerous_keywords:
            assert keyword not in source.lower(), f"Found suspicious keyword: {keyword}"

    def test_all_returns_are_consistent(self) -> None:
        """Verify all functions return mock/parody data."""
        import hack_evm.core as core

        # Test hack always returns 'failed' status
        for level in ["basic", "advanced", "expert", "god_mode"]:
            result = core.hack(level=level)
            assert result["status"] == "failed"
            assert "reason" in result

        # Test quantum always fails
        result = core.quantum_mode()
        assert result["status"] == "failed"

        # Test time machine creates paradox, not actual hacks
        result = core.time_machine()
        assert result["status"] == "paradox_created"

    def test_all_functions_are_type_annotated(self) -> None:
        """Verify all public functions have type hints (satire with quality)."""
        import hack_evm.core as core

        public_functions = [
            obj
            for name, obj in inspect.getmembers(core)
            if inspect.isfunction(obj) and not name.startswith("_")
        ]
        for func in public_functions:
            annotations = func.__annotations__
            assert (
                "return" in annotations
            ), f"Function {func.__name__} missing return type annotation"

    def test_no_network_calls_possible(self) -> None:
        """Verify the package cannot make network calls."""
        import hack_evm.core as core

        source = inspect.getsource(core)
        assert "requests." not in source
        assert "urllib." not in source
        assert "http." not in source
        assert "ftp." not in source

    def test_disclaimer_in_docstring(self) -> None:
        """Verify disclaimer is present in module docstrings."""
        import hack_evm

        # The docstring might be None if imported as namespace package
        if hack_evm.__doc__ is not None:
            doc_lower = hack_evm.__doc__.lower()
            assert "satire" in doc_lower or "parody" in doc_lower
            assert "no" in doc_lower or "not" in doc_lower
        else:
            # Check the __init__.py file directly
            from pathlib import Path

            init_file = Path(__file__).parent.parent / "hack_evm" / "__init__.py"
            content = init_file.read_text().lower()
            assert "satire" in content or "parody" in content

    def test_purely_entertainment_purpose(self) -> None:
        """Verify the code is clearly entertainment/satire only."""
        import hack_evm.core as core

        source = inspect.getsource(core)
        joke_indicators = ["[bold", "Panel(", "console.print", "random.choice"]
        for indicator in joke_indicators:
            assert indicator in source, f"Missing expected satire element: {indicator}"
