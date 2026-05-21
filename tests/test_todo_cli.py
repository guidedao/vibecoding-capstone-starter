from todo_cli import main


def test_list_outputs_all_tasks(capsys):
    main(["list"])

    output = capsys.readouterr().out

    assert "[x] написать спеку" in output
    assert "[ ] ревью диффа" in output

