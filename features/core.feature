Feature: Functionality of jrnl outside of actually handling journals

    Scenario: Displaying the version number
        Given we use the config "simple.yaml"
        When we run "jrnl --version"
        Then we should get no error
        Then the output should match "^minchin.jrnl, version \d+\.\d+(\.\d+)?(-(alpha|beta)\d*)?"

    Scenario: Displaying the version number
        Given we use the config "simple.yaml"
        When we run "jrnl -v"
        Then we should get no error
        Then the output should match "^minchin.jrnl, version \d+\.\d+(\.\d+)?(-(alpha|beta)\d*)?"

    Scenario: Running the diagnostic command
        When we run "jrnl --diagnostic"
        Then the output should contain "minchin.jrnl"
        And the output should contain "Python"

    @todo
    Scenario: Listing available journals
