class TaskPlanner:

    def __init__(
        self,
        position_tolerance=5,
        required_stable_frames=3
    ):
        # 允许目标在 x / y 方向上的最大位置变化
        self.position_tolerance = position_tolerance

        # 连续稳定多少次以后，才认为目标真正稳定
        self.required_stable_frames = required_stable_frames

        # 保存上一帧目标中心
        self.previous_center = None

        # 当前连续稳定次数
        self.stable_count = 0


    def select_target(
        self,
        results
    ):
        """
        从检测结果中选择需要处理的目标
        """

        # 没有任何检测结果
        if not results:

            print(
                "没有检测到目标"
            )

            return None


        # 保存符合要求的目标
        valid_results = []

        for result in results:

            # 目前仍然使用面积 > 500
            # 作为有效目标判断条件
            if result.is_valid(500):

                valid_results.append(
                    result
                )


        # 检测到了轮廓，
        # 但是没有符合要求的目标
        if not valid_results:

            print(
                "没有符合要求的有效目标"
            )

            return None


        # 从所有有效目标中
        # 选择面积最大的目标
        largest_target = max(
            valid_results,
            key=lambda result: result.area
        )


        print(
            "任务规划器选择目标：",
            largest_target.center
        )


        return largest_target


    def is_target_stable(
        self,
        detection_result
    ):
        """
        判断目标是否已经连续多帧保持稳定
        """

        # 当前帧目标中心
        current_center = (
            detection_result.center
        )


        # =========================
        # 第一次检测
        # =========================

        if self.previous_center is None:

            # 第一次只有当前帧，
            # 没有上一帧可以比较
            self.previous_center = (
                current_center
            )

            print(
                "记录第一帧目标：",
                current_center
            )

            return False


        # =========================
        # 计算当前位置和上一帧的位置差
        # =========================

        distance_x = abs(
            current_center[0]
            -
            self.previous_center[0]
        )

        distance_y = abs(
            current_center[1]
            -
            self.previous_center[1]
        )


        # 当前帧比较结束后，
        # 当前中心成为下一次的上一帧中心
        self.previous_center = (
            current_center
        )


        # =========================
        # 判断这一帧是否稳定
        # =========================

        stable = (
            distance_x
            <=
            self.position_tolerance

            and

            distance_y
            <=
            self.position_tolerance
        )


        # =========================
        # 更新连续稳定次数
        # =========================

        if stable:

            self.stable_count += 1

            print(
                "连续稳定次数：",
                self.stable_count
            )

        else:

            # 只要中间出现一次明显偏移，
            # “连续稳定”就被打断
            self.stable_count = 0

            print(
                "目标位置变化较大，稳定计数清零"
            )


        # =========================
        # 是否达到稳定要求
        # =========================

        if (
            self.stable_count
            >=
            self.required_stable_frames
        ):

            print(
                "目标已连续多帧稳定"
            )

            return True


        return False