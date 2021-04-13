# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases/get_token.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseGetToken(HttpRunner):

    config = (
        Config("get token testcase with functions")
        .variables(
            **{
                "corpid": "ww6c7ef90c916657d9",
                "corpsecret": "JPEu7UoM2Fd-xTvU65Mut4YmcUP1ZLEOiznvh02NHZE",
            }
        )
        .base_url("https://qyapi.weixin.qq.com/cgi-bin")
    )

    teststeps = [
        Step(
            RunRequest("get token with params")
            .get("gettoken")
            .with_params(**{"corpid": "$corpid", "corpsecret": "$corpsecret"})
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseGetToken().test_start()
