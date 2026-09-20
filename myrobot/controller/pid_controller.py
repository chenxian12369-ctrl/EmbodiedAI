class PIDController:

    def __init__(
        self,
        kp,
        ki,
        kd,
        integral_limit=300
    ):

        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.integral_limit = (
            integral_limit
        )

        self.integral = 0.0

        self.previous_error = None
    def update(
    self,
    error
):

        # P
        p_output = (
            self.kp * error
        )

        # I
        self.integral += error

        self.integral = max(
            -self.integral_limit,
            min(
                self.integral,
                self.integral_limit
            )
        )

        i_output = (
            self.ki * self.integral
        )

        # D
        if self.previous_error is None:

            derivative = 0.0

        else:

            derivative = (
                error
                - self.previous_error
            )

        d_output = (
            self.kd * derivative
        )

        # 保存本轮误差
        self.previous_error = error

        # PID总输出
        control = (
            p_output
            + i_output
            + d_output
        )

        return control
    def reset(self):

        self.integral = 0.0

        self.previous_error = None