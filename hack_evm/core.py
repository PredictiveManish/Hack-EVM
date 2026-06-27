"""
Core hacking engine for hack-evm.

Contains all the sophisticated, quantum-enhanced, blockchain-powered,
AI-driven hacking algorithms that absolutely do not work.
"""

import random
import time
from typing import Any, Literal

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

# Initialize rich console for beautiful terminal output
console = Console()

# Global flag to skip delays (used by tests)
_fast_mode: bool = False


def set_fast_mode(enabled: bool = True) -> None:
    """Enable or disable fast mode for testing."""
    global _fast_mode
    _fast_mode = enabled


# Collection of sophisticated hacking steps that definitely work (not)
SOPHISTICATED_STEPS: list[str] = [
    "Initializing quantum entanglement with EVM...",
    "Connecting to secret satellite network...",
    "Contacting anonymous hacker collective...",
    "Downloading votes from cloud...",
    "Establishing blockchain backdoor...",
    "Activating neural network vote predictor...",
    "Bypassing quantum encryption...",
    "Synchronizing with time server for temporal attack...",
    "Loading Bollywood cyber toolkit...",
    "Consulting ancient hacking manuscripts...",
    "Calculating reverse quantum blockchain...",
    "Deploying AI-powered democracy extractor...",
    "Establishing TCP/IP over carrier pigeon...",
    "Decrypting votes with machine learning...",
    "Running zero-day exploit (day -1)...",
    "Activating stealth mode (invisible to democracy)...",
    "Connecting to dark web vote market...",
    "Synthesizing quantum key from memes...",
    "Loading hacker matrix rain effect...",
    "Defragmenting blockchain with cyber attacks...",
]

# Collection of ridiculous failure reasons
FAILURE_REASONS: list[str] = [
    "EVM is not connected to the internet.",
    "Operation failed successfully.",
    "The EVM was manufactured before the internet existed.",
    "Battery low. EVM is sleeping.",
    "The EVM has a strong password: 'password123'. Too strong.",
    "Quantum decoherence: The EVM observed itself.",
    "Democracy firewall detected your shenanigans.",
    "The EVM is running on Windows 95. No known exploits.",
    "Votes are encrypted with ROT13. Unbreakable.",
    "Your hacking license has expired.",
    "EVM requires CAPTCHA verification. Are you a robot?",
    "The EVM is in airplane mode.",
    "Network timeout: EVM is buffering democracy.",
    "The constitution blocked your request.",
    "EVM firmware updated. Now it's running Doom.",
    "Bollywood cyber toolkit crashed. Too much drama.",
    "Your quantum computer needs a software update.",
    "The satellite fell out of orbit. Literally.",
    "EVM is protected by a very angry looking squirrel.",
    "Divide by zero error in democracy calculation.",
]

# Easter egg modes
CONSPIRACY_THEORIES: list[str] = [
    "The EVM is actually a toaster with buttons.",
    "All votes are stored on a floppy disk in Area 51.",
    "The real EVM was replaced by a lizard person in 2004.",
    "Every EVM has a tiny parliament inside it.",
    "Votes are counted by trained parrots in a secret bunker.",
    "The 'close' button actually orders pizza.",
    "EVM stands for 'Extraordinary Vending Machine'.",
    "The voter-verified paper audit trail is just a receipt for Amazon.",
    "All EVMs are connected to a Windows XP server in a cave.",
    "The ballot button is actually a subscription to a newsletter.",
]

ALIEN_TECHNOLOGY: list[str] = [
    "👽 Activating alien technology...\n[*] Ancient aliens have confirmed: EVMs are too primitive for their tech.\n[*] Even the greys couldn't hack this.",
    "🛸 Contacting mothership...\n[*] Aliens responded: 'We hack galaxies, not democracies.'\n[*] They suggested trying a different planet.",
    "🌌 Scanning for extraterrestrial exploits...\n[*] Found one! But it only works on Martian voting machines.\n[*] Earth EVMs use a different standard.",
]

TIME_MACHINE_ATTEMPTS: list[str] = [
    "⏰ Activating temporal displacement...\n[*] Traveled to 2014 to hack EVM during elections.\n[*] Discovered time machine runs on VBScript. Crashed in 2015.",
    "⌛ Spinning up flux capacitor...\n[*] Arrived in 1947. No EVMs yet. Found a typewriter instead.\n[*] Hacked the typewriter successfully though.",
    "🕰️ Initiating chronological bypass...\n[*] Went back 5 minutes to hack before you started.\n[*] Created temporal paradox. Universe.exe has stopped working.",
]

BOLLYWOOD_MODE: list[str] = [
    "🎬 BOLLYWOOD HACK SEQUENCE INITIATED...\n[*] Dramatic background music playing...\n[*] Protagonist typing furiously on keyboard...\n[*] Six monitors showing meaningless green text...\n[*] Heroine enters: 'Ruko! EVM ko hack mat karo!' (Stop! Don't hack the EVM!)\n[*] It's too late. We've already fallen in love with the EVM.\n[*] Climactic twist: The EVM was the hero's long-lost twin all along!",
    "🎵 Cue the background dancers...\n[*] 500 extras appear out of nowhere\n[*] They're all better hackers than you\n[*] But they're too busy dancing\n[*] Hack cancelled due to spontaneous dance number",
    "🇮🇳 Loading desi jugaad...\n[*] Applied pressure cooker technique\n[*] EVM started making biryani\n[*] Hack failed, but dinner is served!",
]


def _get_version() -> str:
    """Get the package version safely."""
    try:
        from hack_evm import __version__

        return __version__
    except ImportError:
        return "0.1.0"


def _animate_steps(steps: list[str], delay: float = 0.5) -> None:
    """
    Animate a list of steps with a typewriter effect.

    Args:
        steps: List of step messages to display
        delay: Delay between steps in seconds
    """
    effective_delay = 0 if _fast_mode else delay
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]Preparing hack...", total=len(steps))
        for step in steps:
            time.sleep(effective_delay)
            progress.update(task, description=f"[yellow][*] {step}")
            progress.advance(task)


def _get_random_failure() -> str:
    """Get a random failure message from the collection."""
    return random.choice(FAILURE_REASONS)


def _display_banner() -> None:
    """Display the hack-evm ASCII banner."""
    banner = f"""
    ⚡ HACK-EVM v{_get_version()} ⚡
    "Hacking Democracy, One Laugh at a Time"
    """
    console.print(banner, style="bold yellow")
    console.print("─" * 60, style="dim")


def hack(level: Literal["basic", "advanced", "expert", "god_mode"] = "basic") -> dict[str, Any]:
    """
    Attempt to hack an EVM with varying levels of sophistication.

    This function simulates a highly sophisticated hacking operation that
    always fails in a humorous way. No actual hacking is performed.

    Args:
        level: The hacking skill level. Options:
            - "basic": Simple hack attempt (default)
            - "advanced": More sophisticated attempt
            - "expert": Uses quantum computing and blockchain
            - "god_mode": Attempts reality manipulation

    Returns:
        A dictionary containing the operation status and failure details.

    Raises:
        ValueError: If an invalid level is provided.

    Example:
        >>> result = hack(level="expert")
        >>> print(result["status"])
        'failed'
    """
    valid_levels = {"basic", "advanced", "expert", "god_mode"}
    if level not in valid_levels:
        raise ValueError(
            f"Invalid level '{level}'. Must be one of: {', '.join(sorted(valid_levels))}"
        )

    _display_banner()

    # Select steps based on level
    num_steps = {"basic": 5, "advanced": 8, "expert": 12, "god_mode": 15}
    selected_steps = random.sample(
        SOPHISTICATED_STEPS, min(num_steps[level], len(SOPHISTICATED_STEPS))
    )

    if level == "god_mode":
        selected_steps.insert(0, "Attempting to hack reality itself...")
        selected_steps.append("Reconfiguring the matrix...")

    # Animate the hacking steps
    _animate_steps(selected_steps)

    # Add a dramatic pause
    console.print("\n[bold red]✗ OPERATION FAILED[/bold red]")
    time.sleep(1)

    # Generate failure message
    failure_reason = _get_random_failure()

    if level == "expert":
        failure_reason = f"[Expert Analysis] {failure_reason}"
    elif level == "god_mode":
        failure_reason = f"[GOD MODE] Even divine intervention couldn't help. {failure_reason}"

    # Display failure panel
    panel = Panel(
        f"[bold red]FAILED[/bold red]\n"
        f"Reason: [yellow]{failure_reason}[/yellow]\n"
        f"Suggestion: [dim]{_get_suggestion()}[/dim]",
        title="Hack Result",
        border_style="red",
    )
    console.print(panel)

    return {
        "status": "failed",
        "level": level,
        "reason": failure_reason,
        "steps_attempted": len(selected_steps),
        "success_probability": f"{random.uniform(0, 0.0001):.10f}%",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    }


def quantum_mode() -> dict[str, Any]:
    """
    Attempt to hack an EVM using quantum computing principles.

    This function leverages quantum entanglement, superposition,
    and other buzzwords to attempt the impossible. Spoiler: it fails.

    Returns:
        A dictionary with the quantum operation status.

    Example:
        >>> result = quantum_mode()
        >>> result["quantum_state"]
        'collapsed'
    """
    console.print(
        Panel(
            "[bold cyan]🌌 QUANTUM MODE ACTIVATED[/bold cyan]\n"
            '"Schrödinger\'s Vote - Both Counted and Not Counted"',
            border_style="cyan",
        )
    )

    quantum_steps = [
        "Opening quantum tunnel to EVM...",
        "Superposing all possible votes...",
        "Entangling with ballot unit...",
        "Observing quantum state (this might take a while)...",
        "Calculating quantum probability amplitude...",
        "Applying quantum Fourier transform to democracy...",
        "Checking if Schrödinger's cat voted...",
    ]

    _animate_steps(quantum_steps, delay=0.4)

    # Special quantum failure
    quantum_failures = [
        "The quantum state collapsed into 'nice try, lol.'",
        "Heisenberg's uncertainty principle: You can know the vote or the hacker, but not both.",
        "Quantum decoherence: The EVM observed itself.",
        "The cat is both dead and alive, but neither state involves hacking success.",
        "Quantum entanglement failed: The EVM is entangled with a potato.",
    ]

    failure_reason = random.choice(quantum_failures)

    panel = Panel(
        f"[bold red]✗ QUANTUM DECOHERENCE DETECTED[/bold red]\n"
        f"Reason: [yellow]{failure_reason}[/yellow]\n"
        f"Quantum State: [dim]collapsed[/dim]\n"
        f"Probability of success: [dim]|ψ|² ≈ 0[/dim]",
        title="Quantum Hack Result",
        border_style="magenta",
    )
    console.print(panel)

    return {
        "status": "failed",
        "mode": "quantum",
        "reason": failure_reason,
        "quantum_state": "collapsed",
        "wave_function": "ψ(x) = 0",
        "entangled_with": random.choice(["EVM", "potato", "cat", "nothing"]),
    }


def explain() -> str:
    """
    Provide a detailed explanation of why the hacking attempt failed.

    This function generates a pseudo-technical explanation that sounds
    sophisticated but is complete nonsense.

    Returns:
        A string containing the explanation.

    Example:
        >>> explanation = explain()
        >>> "Here's what went wrong" in explanation
        True
    """
    explanations = [
        "The EVM uses a proprietary protocol called 'Not-Connected-To-Anything v2.0'.\n"
        "This makes remote hacking approximately as effective as shouting at the EVM.",
        "Our quantum computer tried to entangle with the EVM, but the EVM's\n"
        "quantum state was 'do not disturb'. Very rude.",
        "The blockchain backdoor was blocked by a firewall made of actual blocks\n"
        "and chains. Physical security: 1, Cyber security: 0.",
        "We attempted a zero-day exploit, but the EVM's calendar was set to 1970.\n"
        "Apparently, it's been zero-day for 50+ years.",
        "The Bollywood cyber toolkit got distracted by a dramatic plot twist\n"
        "and forgot what it was supposed to be hacking.",
        "Our AI determined that the EVM is actually a very sophisticated\n"
        "paperweight. Hacking paperweights is surprisingly difficult.",
    ]

    explanation = random.choice(explanations)

    console.print(
        Panel(
            f"[bold cyan]📚 Here's what went wrong:[/bold cyan]\n\n[yellow]{explanation}[/yellow]",
            title="Failure Analysis",
            border_style="cyan",
        )
    )

    return explanation


def conspiracy(level: int = 1) -> dict[str, Any]:
    """
    Generate random conspiracy theories about EVMs.

    Args:
        level: Intensity level of the conspiracy (1-9000). Higher = more ridiculous.

    Returns:
        Dictionary containing the conspiracy theory.

    Raises:
        ValueError: If level is less than 1.
    """
    if level < 1:
        raise ValueError("Conspiracy level must be at least 1. We're not amateurs here.")

    if level > 9000:
        console.print("[bold yellow]⚠️ It's over 9000!!![/bold yellow]")

    theory = random.choice(CONSPIRACY_THEORIES)

    if level > 100:
        theory += f"\nAlso, the EVM is secretly powered by {level} hamsters on wheels."
    if level > 1000:
        theory += "\nThe hamsters are actually government agents."
    if level > 5000:
        theory += "\nThe government agents are aliens disguised as hamsters."
    if level > 8000:
        theory += "\nThe aliens report to a sentient EVM from the future."

    console.print(
        Panel(
            f"[bold green]🕵️ CONSPIRACY THEORY (Level {level}):[/bold green]\n\n"
            f"[yellow]{theory}[/yellow]",
            title="Top Secret",
            border_style="green",
        )
    )

    return {
        "level": level,
        "theory": theory,
        "plausibility": f"{random.uniform(0, 0.001):.5f}%",
        "cover_up_probability": "100%",
    }


def alien_mode() -> str:
    """
    Activate alien technology hacking mode. Easter egg function.

    Returns:
        A string describing the alien encounter.
    """
    scenario = random.choice(ALIEN_TECHNOLOGY)

    console.print(
        Panel(
            f"[bold green]{scenario}[/bold green]",
            title="👽 ALIEN MODE",
            border_style="green",
        )
    )

    return "Aliens have left the chat."


def time_machine() -> dict[str, Any]:
    """
    Attempt to hack EVM using time travel. Easter egg function.

    Returns:
        Dictionary with time travel results.
    """
    scenario = random.choice(TIME_MACHINE_ATTEMPTS)

    console.print(
        Panel(
            f"[bold blue]{scenario}[/bold blue]",
            title="⏰ TIME MACHINE MODE",
            border_style="blue",
        )
    )

    return {
        "status": "paradox_created",
        "timeline": "broken",
        "grandfather": "confused",
        "recommendation": "Stick to present-day hacking failures.",
    }


def bollywood_mode() -> str:
    """
    Activate Bollywood-style hacking sequence. Easter egg function.

    Returns:
        The script of the dramatic Bollywood scene.
    """
    scene = random.choice(BOLLYWOOD_MODE)

    console.print(
        Panel(
            f"[bold magenta]{scene}[/bold magenta]",
            title="🎬 BOLLYWOOD MODE",
            border_style="magenta",
        )
    )

    return "🎵 *Dramatic exit music plays* 🎵"


def _get_suggestion() -> str:
    """Get a random unhelpful suggestion."""
    suggestions = [
        "Try turning the EVM off and on again.",
        "Maybe ask nicely?",
        "Have you tried using a bigger monitor?",
        "Update your hacking drivers.",
        "The problem exists between keyboard and chair.",
        "Sacrifice a keyboard to the tech gods.",
        "Blow on the EVM's cartridge.",
        "Try Ctrl+Alt+Del on the EVM.",
        "Download more RAM for your hacking rig.",
        "Use the Force, Luke.",
    ]
    return random.choice(suggestions)
