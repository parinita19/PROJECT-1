from app.tasks import task_a3

def test_task_a3():
    # Prepare a test file for dates.txt
    test_data = "2025-02-12\n2025-02-11\n2025-02-05\n2025-02-04\n"
    with open("data/dates.txt", "w", encoding="utf-8") as f:
        f.write(test_data)
    result = task_a3.run()
    assert "Wednesdays" in result