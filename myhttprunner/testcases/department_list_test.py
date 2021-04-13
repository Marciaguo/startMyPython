# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases/department_list.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseDepartmentList(HttpRunner):

    config = (
        Config("get department list")
        .variables(
            **{
                "access_token": "qVGAbYpA7Sitt6MC5098rchEiTaWdmEaGjkjf_3ImgqOLL4BfewteFb6zcN_waigpCgePaWVaKb49d-L9RJwssmB-oWPLw10yYAOu70N2ZbVLcbnVT40H7NEMFNdE4n2zvs2wjCjK8hWlbn3xPtx82ktjPkjYBYTY_YNVuaG5Mg24sVLG6cc_RD0_KPq3k6Lks-2yJagUbzD4t_6ye9c9w",
                "id": 1,
            }
        )
        .base_url("https://qyapi.weixin.qq.com/cgi-bin/department")
    )

    teststeps = [
        Step(
            RunRequest("get token with params")
            .get("list")
            .with_params(**{"access_token": "$access_token", "id": "$id"})
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseDepartmentList().test_start()