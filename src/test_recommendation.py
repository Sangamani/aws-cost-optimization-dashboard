from src.scanner import get_instances
from src.recommendations import analyze_instance

print("Starting recommendation analysis...")

instances = get_instances()

for instance in instances:

    result = analyze_instance(instance)

    print("\nInstance:")
    print(instance)

    print("Recommendations:")
    print(result)

print("\nAnalysis completed.")