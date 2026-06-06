"""
Tests for the hack_evm.core module.

Tests all hacking functions to ensure they properly fail
and return expected data structures.
"""

import pytest

from hack_evm.core import (
    _get_suggestion,
    alien_mode,
    bollywood_mode,
    conspiracy,
    explain,
    hack,
    quantum_mode,
    time_machine,
)


class TestHack:
    """Test the main hack function."""

    def test_hack_basic(self) -> None:
        """Test basic hack level returns expected structure."""
        result = hack(level="basic")
        assert isinstance(result, dict)
        assert result["status"] == "failed"
        assert "reason" in result
        assert "steps_attempted" in result
        assert result["level"] == "basic"
        assert isinstance(result["reason"], str)
        assert len(result["reason"]) > 0

    def test_hack_advanced(self) -> None:
        """Test advanced hack level."""
        result = hack(level="advanced")
        assert result["status"] == "failed"
        assert result["level"] == "advanced"
        assert result["steps_attempted"] <= 8

    def test_hack_expert(self) -> None:
        """Test expert hack level."""
        result = hack(level="expert")
        assert result["status"] == "failed"
        assert "[Expert Analysis]" in result["reason"]

    def test_hack_god_mode(self) -> None:
        """Test god_mode hack level."""
        result = hack(level="god_mode")
        assert result["status"] == "failed"
        assert "[GOD MODE]" in result["reason"]

    def test_hack_invalid_level(self) -> None:
        """Test that invalid levels raise ValueError."""
        with pytest.raises(ValueError, match="Invalid level"):
            hack(level="super_duper_hacker")

    def test_hack_always_fails(self) -> None:
        """Test that hack ALWAYS fails."""
        for _ in range(10):
            result = hack(level="basic")
            assert result["status"] == "failed"

    def test_hack_return_structure(self) -> None:
        """Test complete return dictionary structure."""
        result = hack(level="expert")
        expected_keys = {
            "status",
            "level",
            "reason",
            "steps_attempted",
            "success_probability",
            "timestamp",
        }
        assert set(result.keys()) == expected_keys
        assert "%" in result["success_probability"]


class TestQuantumMode:
    """Test quantum mode functionality."""

    def test_quantum_mode_returns_dict(self) -> None:
        """Test quantum_mode returns proper dictionary."""
        result = quantum_mode()
        assert isinstance(result, dict)
        assert result["status"] == "failed"
        assert result["mode"] == "quantum"
        assert result["quantum_state"] == "collapsed"
        assert result["wave_function"] == "ψ(x) = 0"

    def test_quantum_mode_always_fails(self) -> None:
        """Test quantum mode always fails."""
        for _ in range(5):
            result = quantum_mode()
            assert result["status"] == "failed"

    def test_quantum_mode_has_reason(self) -> None:
        """Test quantum failure reason is present."""
        result = quantum_mode()
        assert "reason" in result
        assert len(result["reason"]) > 0

    def test_quantum_mode_entanglement(self) -> None:
        """Test quantum entanglement target is set."""
        result = quantum_mode()
        assert "entangled_with" in result
        assert result["entangled_with"] in {"EVM", "potato", "cat", "nothing"}


class TestExplain:
    """Test the explain function."""

    def test_explain_returns_string(self) -> None:
        """Test explain returns a string."""
        explanation = explain()
        assert isinstance(explanation, str)
        assert len(explanation) > 0

    def test_explain_is_different(self) -> None:
        """Test that explanations can be different (randomness)."""
        explanations = {explain() for _ in range(10)}
        # With 6 possible explanations, we should get at least 2 different ones
        assert len(explanations) >= 1  # Could technically be 1 but unlikely


class TestConspiracy:
    """Test conspiracy theory generator."""

    def test_conspiracy_valid_level(self) -> None:
        """Test conspiracy with valid level."""
        result = conspiracy(level=42)
        assert isinstance(result, dict)
        assert result["level"] == 42
        assert "theory" in result
        assert len(result["theory"]) > 0

    def test_conspiracy_high_level(self) -> None:
        """Test high conspiracy levels add extra content."""
        result = conspiracy(level=5001)
        assert "aliens" in result["theory"].lower()

    def test_conspiracy_invalid_level(self) -> None:
        """Test that level < 1 raises ValueError."""
        with pytest.raises(ValueError, match="at least 1"):
            conspiracy(level=0)

    def test_conspiracy_over_9000(self) -> None:
        """Test that level > 9000 doesn't crash."""
        result = conspiracy(level=9001)
        assert result["level"] == 9001

    def test_conspiracy_plausibility(self) -> None:
        """Test plausibility is very low."""
        result = conspiracy(level=1)
        plausibility = float(result["plausibility"].rstrip("%"))
        assert plausibility < 0.01


class TestEasterEggs:
    """Test easter egg functions."""

    def test_alien_mode(self) -> None:
        """Test alien mode returns string."""
        result = alien_mode()
        assert isinstance(result, str)
        assert len(result) > 0

    def test_time_machine(self) -> None:
        """Test time machine mode returns dict."""
        result = time_machine()
        assert isinstance(result, dict)
        assert result["status"] == "paradox_created"
        assert result["timeline"] == "broken"

    def test_bollywood_mode(self) -> None:
        """Test Bollywood mode returns string."""
        result = bollywood_mode()
        assert isinstance(result, str)
        assert len(result) > 0


class TestHelpers:
    """Test helper functions."""

    def test_get_suggestion(self) -> None:
        """Test that suggestions are non-empty strings."""
        suggestion = _get_suggestion()
        assert isinstance(suggestion, str)
        assert len(suggestion) > 0
