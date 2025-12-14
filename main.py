# main.py (Insert this code block at the top)
import sys
import os

# Get the directory of the current script (project root)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the project root to the system path
if current_dir not in sys.path:
    sys.path.append(current_dir)

# Now, the rest of your imports will work:
from agents.coordinator import Coordinator 
# ... rest of your code

def run_scenario(coordinator, query, filename):
    """Runs a single query and saves the output to the required file."""
    print(f"\n========================================================")
    print(f" SCENARIO: {filename.replace('.txt', '').upper().replace('_', ' ')}")
    print(f" USER QUERY: {query}")
    print(f"========================================================\n")
    
    # Capture the full execution trace
    # (Note: You need to set up your agents to print their logs/traces to the console)
    
    # This is a basic way to capture output, for a production system you'd use a Logger.
    # For this assignment, redirecting standard output (stdout) is a common way 
    # to capture the console trace for the deliverable.
    
    # In a real environment, you might temporarily redirect stdout to a file:
    # import sys
    # original_stdout = sys.stdout
    # with open(f"outputs/{filename}", 'w') as f:
    #     sys.stdout = f
    #     final_answer = coordinator.process_query(query)
    #     print(f"\nFINAL SYSTEM RESPONSE: {final_answer}")
    #     sys.stdout = original_stdout # Restore original stdout

    # For simplicity here, we'll just print and you manually copy the trace for now
    # or implement the stdout redirection above.
    
    final_answer = coordinator.process_query(query)
    
    # Placeholder for saving trace to file (implement the block above)
    with open(f"outputs/{filename}", 'a') as f:
         f.write(f"USER QUERY: {query}\n")
         f.write(f"FINAL RESPONSE: {final_answer}\n")
         f.write("--- (Insert full console trace above) ---\n\n")

    print(f"\n[SYSTEM RESPONSE]: {final_answer}")
    print(f"Trace saved (or needs to be copied) to outputs/{filename}")


if __name__ == "__main__":
    # Ensure the outputs directory exists
    os.makedirs("outputs", exist_ok=True)
    
    # 1. Instantiate the Coordinator
    manager = Coordinator()

    # 2. Define the Test Scenarios [cite: 71, 72-82]
    scenarios = [
        ("What are the main types of neural networks?", "simple_query.txt"),
        ("Research transformer architectures, analyze their computational efficiency, and summarize key trade-offs.", "complex_query.txt"),
        ("Find recent papers on reinforcement learning, analyze their methodologies, and identify common challenges.", "multi_step.txt"),
        ("Compare two machine-learning approaches and recommend which is better for our use case.", "collaborative.txt"),
        # IMPORTANT: Run the memory test scenario LAST, after you've stored some facts.
        ("What did we discuss about neural networks earlier?", "memory_test.txt"), 
    ]

    # 3. Execute all scenarios
    for query, filename in scenarios:
        run_scenario(manager, query, filename)

    print("\n\nAll test scenarios completed. Check your outputs/ folder!")