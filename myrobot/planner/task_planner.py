class TaskPlanner:

    def select_target(self, results):
        """
        从检测结果中选择面积最大的有效目标
        """

        if not results:
            print("没有检测到目标")
            return None

        valid_results = []

        for result in results:

            if result.is_valid(500):
                valid_results.append(result)

        if not valid_results:
            print("没有符合要求的有效目标")
            return None

        largest_target = max(
            valid_results,
            key=lambda result: result.area
        )

        print(
            "任务规划器选择目标：",
            largest_target.center
        )

        return largest_target