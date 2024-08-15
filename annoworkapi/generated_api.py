# ruff: noqa: E501, ANN401
# flake8: noqa: W291
# pylint: disable=too-many-lines,trailing-whitespace

"""
AbstractAnnoworkApiのヘッダ部分

Note:
    このファイルはopenapi-generatorで自動生成される。詳細は generate/README.mdを参照
"""

import abc
from typing import Any, Optional  # pylint: disable=unused-import


class AbstractAnnoworkApi(abc.ABC):
    """
    AnnoworkApiクラスの抽象クラス
    """

    @abc.abstractmethod
    def _request_wrapper(
        self,
        http_method: str,
        url_path: str,
        *,
        query_params: Optional[dict[str, Any]] = None,
        header_params: Optional[dict[str, Any]] = None,
        request_body: Optional[Any] = None,
        log_response_with_error: bool = True,
    ) -> Any:
        pass

    #########################################
    # Public Method : AccountApi
    # NOTE: This method is auto generated by OpenAPI Generator
    #########################################

    def confirm_reset_password(self, request_body: Optional[Any] = None, **kwargs) -> Any:
        """パスワードリセットstep2（新しいパスワードに変更）




        新しいパスワードに変更します。 本人確認のため、[パスワードリセットを要求](#operation/resetPassword)で受信したメールに記載された検証コードを使用します。  パスワードリセットプロセスの最終ステップです。

        Args:
            request_body (Any): Request Body
                confirm_reset_password_request (ConfirmResetPasswordRequest):  (required)

        Returns:
            InlineResponse200


        """
        url_path = "/confirm-reset-password"
        http_method = "POST"
        keyword_params: dict[str, Any] = {
            "request_body": request_body,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def confirm_sign_up(self, request_body: Optional[Any] = None, **kwargs) -> Any:
        """サインアップstep2（本登録）




        アカウントのサインアップの最後のステップとして、アカウントを本登録します。

        Args:
            request_body (Any): Request Body
                confirm_sign_up_request (ConfirmSignUpRequest):  (required)

        Returns:
            InlineResponse200


        """
        url_path = "/confirm-sign-up"
        http_method = "POST"
        keyword_params: dict[str, Any] = {
            "request_body": request_body,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def get_account_external_linkage_info(self, user_id: str, **kwargs) -> Any:
        """アカウント外部連携情報取得





        Args:
            user_id (str):  ユーザーID (required)

        Returns:
            InlineResponse2001


        """
        url_path = f"/accounts/{user_id}/external-linkage-info"
        http_method = "GET"
        keyword_params: dict[str, Any] = {}
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def put_account_external_linkage_info(self, user_id: str, request_body: Optional[Any] = None, **kwargs) -> Any:
        """アカウント外部連携情報更新





        Args:
            user_id (str):  ユーザーID (required)
            request_body (Any): Request Body
                put_account_external_linkage_info_request (PutAccountExternalLinkageInfoRequest):  (required)

        Returns:
            InlineResponse2001


        """
        url_path = f"/accounts/{user_id}/external-linkage-info"
        http_method = "PUT"
        keyword_params: dict[str, Any] = {
            "request_body": request_body,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def reset_password(self, request_body: Optional[Any] = None, **kwargs) -> Any:
        """パスワードリセットstep1（開始）




        パスワードリセットに必要な確認コードをメールで送付します。 後続の[新しいパスワードに変更](#operation/confirmResetPassword)を実行することで、新しいパスワードに変更できます。

        Args:
            request_body (Any): Request Body
                reset_password_request (ResetPasswordRequest):  (required)

        Returns:
            InlineResponse200


        """
        url_path = "/reset-password"
        http_method = "POST"
        keyword_params: dict[str, Any] = {
            "request_body": request_body,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def sign_up(self, request_body: Optional[Any] = None, **kwargs) -> Any:
        """サインアップstep1（仮登録）




        アカウントのサインアップの最初のステップとして、アカウントを仮登録します。  Annoworkに未登録のメールアドレスであれば、新規アカウントが仮登録状態で作成され、本登録フローのためのメールが送信されます。 このメールには仮パスワードなどが記載されています。  指定したメールアドレスを使うユーザーが仮登録であれば、本登録フローのメールが再送信されます。 指定したメールアドレスを使うユーザーが本登録であれば、不正なリクエストとしてエラーを返します（本登録が仮登録に戻ることはありません）。

        Args:
            request_body (Any): Request Body
                sign_up_request (SignUpRequest):  (required)

        Returns:
            InlineResponse200


        """
        url_path = "/sign-up"
        http_method = "POST"
        keyword_params: dict[str, Any] = {
            "request_body": request_body,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    #########################################
    # Public Method : ActualWorkingTimeApi
    # NOTE: This method is auto generated by OpenAPI Generator
    #########################################

    def delete_actual_working_time_by_workspace_member(
        self, workspace_id: str, workspace_member_id: str, actual_working_time_id: str, **kwargs
    ) -> Any:
        """実績時間の削除





        Args:
            workspace_id (str):  ワークスペースID (required)
            workspace_member_id (str):  ワークスペースメンバーID (required)
            actual_working_time_id (str):  実績稼働時間ID (required)

        Returns:
            ActualWorkingTime


        """
        url_path = f"/workspaces/{workspace_id}/members/{workspace_member_id}/actual-working-times/{actual_working_time_id}"
        http_method = "DELETE"
        keyword_params: dict[str, Any] = {}
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def get_actual_working_times(self, workspace_id: str, query_params: Optional[dict[str, Any]] = None, **kwargs) -> Any:
        """ワークスペース全体の実績時間の一括取得





        Args:
            workspace_id (str):  ワークスペースID (required)
            query_params (dict[str, Any]): Query Parameters
                job_id (str):  ジョブID
                term_start (str):  日付での範囲検索で使用
                term_end (str):  日付での範囲検索で使用

        Returns:
            [ActualWorkingTime]


        """
        url_path = f"/workspaces/{workspace_id}/actual-working-times"
        http_method = "GET"
        keyword_params: dict[str, Any] = {
            "query_params": query_params,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def get_actual_working_times_by_workspace_member(
        self, workspace_id: str, workspace_member_id: str, query_params: Optional[dict[str, Any]] = None, **kwargs
    ) -> Any:
        """ワークスペースメンバーに対する実績時間の一括取得





        Args:
            workspace_id (str):  ワークスペースID (required)
            workspace_member_id (str):  ワークスペースメンバーID (required)
            query_params (dict[str, Any]): Query Parameters
                term_start (str):  取得する範囲の開始日時。日付での範囲検索で使用
                term_end (str):  取得する範囲の終了日時。日付での範囲検索で使用

        Returns:
            [ActualWorkingTime]


        """
        url_path = f"/workspaces/{workspace_id}/members/{workspace_member_id}/actual-working-times"
        http_method = "GET"
        keyword_params: dict[str, Any] = {
            "query_params": query_params,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def get_sum_of_actual_working_times(self, workspace_id: str, query_params: Optional[dict[str, Any]] = None, **kwargs) -> Any:
        """ワークスペース全体の実績時間の合計取得





        Args:
            workspace_id (str):  ワークスペースID (required)
            query_params (dict[str, Any]): Query Parameters
                job_id (str):  ジョブID
                includes_archived_job (bool):  アーカイブ化したジョブの合計も含めるかどうか

        Returns:
            SumOfTimes


        """
        url_path = f"/workspaces/{workspace_id}/sum-of-actual-working-times"
        http_method = "GET"
        keyword_params: dict[str, Any] = {
            "query_params": query_params,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def put_actual_working_time_by_workspace_member(
        self,
        workspace_id: str,
        workspace_member_id: str,
        actual_working_time_id: str,
        request_body: Optional[Any] = None,
        **kwargs,
    ) -> Any:
        """実績時間の更新





        Args:
            workspace_id (str):  ワークスペースID (required)
            workspace_member_id (str):  ワークスペースメンバーID (required)
            actual_working_time_id (str):  実績稼働時間ID (required)
            request_body (Any): Request Body
                put_actual_working_time_request (PutActualWorkingTimeRequest):  (required)

        Returns:
            ActualWorkingTime


        """
        url_path = f"/workspaces/{workspace_id}/members/{workspace_member_id}/actual-working-times/{actual_working_time_id}"
        http_method = "PUT"
        keyword_params: dict[str, Any] = {
            "request_body": request_body,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    #########################################
    # Public Method : ExpectedWorkingTimeApi
    # NOTE: This method is auto generated by OpenAPI Generator
    #########################################

    def delete_expected_working_time_by_workspace_member(self, workspace_id: str, workspace_member_id: str, date: str, **kwargs) -> Any:
        """予定稼働時間の日付指定削除





        Args:
            workspace_id (str):  ワークスペースID (required)
            workspace_member_id (str):  ワークスペースメンバーID (required)
            date (str):  予定の対象日 (required)

        Returns:
            ExpectedWorkingTime


        """
        url_path = f"/workspaces/{workspace_id}/members/{workspace_member_id}/expected-working-times/{date}"
        http_method = "DELETE"
        keyword_params: dict[str, Any] = {}
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def get_expected_working_times(self, workspace_id: str, query_params: Optional[dict[str, Any]] = None, **kwargs) -> Any:
        """予定稼働時間の一括取得





        Args:
            workspace_id (str):  ワークスペースID (required)
            query_params (dict[str, Any]): Query Parameters
                term_start (str):  日付での範囲検索で使用
                term_end (str):  日付での範囲検索で使用

        Returns:
            [ExpectedWorkingTime]


        """
        url_path = f"/workspaces/{workspace_id}/expected-working-times"
        http_method = "GET"
        keyword_params: dict[str, Any] = {
            "query_params": query_params,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def get_expected_working_times_by_workspace_member(
        self, workspace_id: str, workspace_member_id: str, query_params: Optional[dict[str, Any]] = None, **kwargs
    ) -> Any:
        """予定稼働時間の一覧取得





        Args:
            workspace_id (str):  ワークスペースID (required)
            workspace_member_id (str):  ワークスペースメンバーID (required)
            query_params (dict[str, Any]): Query Parameters
                term_start (str):  取得する範囲の開始日。日付での範囲検索で使用
                term_end (str):  取得する範囲の終了日。日付での範囲検索で使用

        Returns:
            [ExpectedWorkingTime]


        """
        url_path = f"/workspaces/{workspace_id}/members/{workspace_member_id}/expected-working-times"
        http_method = "GET"
        keyword_params: dict[str, Any] = {
            "query_params": query_params,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def put_expected_working_time_by_workspace_member(
        self, workspace_id: str, workspace_member_id: str, date: str, request_body: Optional[Any] = None, **kwargs
    ) -> Any:
        """予定稼働時間の日付指定更新





        Args:
            workspace_id (str):  ワークスペースID (required)
            workspace_member_id (str):  ワークスペースメンバーID (required)
            date (str):  予定の対象日 (required)
            request_body (Any): Request Body
                put_expected_working_time_request (PutExpectedWorkingTimeRequest):  (required)

        Returns:
            ExpectedWorkingTime


        """
        url_path = f"/workspaces/{workspace_id}/members/{workspace_member_id}/expected-working-times/{date}"
        http_method = "PUT"
        keyword_params: dict[str, Any] = {
            "request_body": request_body,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    #########################################
    # Public Method : JobApi
    # NOTE: This method is auto generated by OpenAPI Generator
    #########################################

    def delete_job(self, workspace_id: str, job_id: str, **kwargs) -> Any:
        """ジョブの削除





        Args:
            workspace_id (str):  ワークスペースID (required)
            job_id (str):  ジョブID (required)

        Returns:
            Job


        """
        url_path = f"/workspaces/{workspace_id}/jobs/{job_id}"
        http_method = "DELETE"
        keyword_params: dict[str, Any] = {}
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def get_job(self, workspace_id: str, job_id: str, **kwargs) -> Any:
        """ジョブの取得





        Args:
            workspace_id (str):  ワークスペースID (required)
            job_id (str):  ジョブID (required)

        Returns:
            Job


        """
        url_path = f"/workspaces/{workspace_id}/jobs/{job_id}"
        http_method = "GET"
        keyword_params: dict[str, Any] = {}
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def get_job_children(self, workspace_id: str, job_id: str, **kwargs) -> Any:
        """子ジョブの一覧取得





        Args:
            workspace_id (str):  ワークスペースID (required)
            job_id (str):  ジョブID (required)

        Returns:
            JobChildren


        """
        url_path = f"/workspaces/{workspace_id}/jobs/{job_id}/children"
        http_method = "GET"
        keyword_params: dict[str, Any] = {}
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def get_jobs(self, workspace_id: str, query_params: Optional[dict[str, Any]] = None, **kwargs) -> Any:
        """ジョブの一覧取得





        Args:
            workspace_id (str):  ワークスペースID (required)
            query_params (dict[str, Any]): Query Parameters
                sort (str):  sort key(複数項目を利用したソートの場合は,(カンマ)区切りで指定してください。key(id or name)、降順にしたい場合は先頭に-(ハイフン)を付ける)

        Returns:
            [Job]


        """
        url_path = f"/workspaces/{workspace_id}/jobs"
        http_method = "GET"
        keyword_params: dict[str, Any] = {
            "query_params": query_params,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def put_job(self, workspace_id: str, job_id: str, request_body: Optional[Any] = None, **kwargs) -> Any:
        """ジョブの更新





        Args:
            workspace_id (str):  ワークスペースID (required)
            job_id (str):  ジョブID (required)
            request_body (Any): Request Body
                put_job_request (PutJobRequest):  (required)

        Returns:
            Job


        """
        url_path = f"/workspaces/{workspace_id}/jobs/{job_id}"
        http_method = "PUT"
        keyword_params: dict[str, Any] = {
            "request_body": request_body,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    #########################################
    # Public Method : LoginApi
    # NOTE: This method is auto generated by OpenAPI Generator
    #########################################

    def post_login(self, request_body: Optional[Any] = None, **kwargs) -> Any:
        """ログイン





        Args:
            request_body (Any): Request Body
                login_request (LoginRequest):  (required)

        Returns:
            LoginToken


        """
        url_path = "/login"
        http_method = "POST"
        keyword_params: dict[str, Any] = {
            "request_body": request_body,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    #########################################
    # Public Method : MyApi
    # NOTE: This method is auto generated by OpenAPI Generator
    #########################################

    def change_password(self, request_body: Optional[Any] = None, **kwargs) -> Any:
        """パスワード変更




        パスワード変更

        Args:
            request_body (Any): Request Body
                change_password_request (ChangePasswordRequest):  (required)

        Returns:
            InlineResponse200


        """
        url_path = "/my/account/password"
        http_method = "POST"
        keyword_params: dict[str, Any] = {
            "request_body": request_body,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def get_my_account(self, **kwargs) -> Any:
        """ログイン中のアカウント情報を取得する





        Args:

        Returns:
            Account


        """
        url_path = "/my/account"
        http_method = "GET"
        keyword_params: dict[str, Any] = {}
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def get_my_schedules(self, query_params: Optional[dict[str, Any]] = None, **kwargs) -> Any:
        """自身がアサインされているスケジュール一覧を取得する





        Args:
            query_params (dict[str, Any]): Query Parameters
                workspace_id (str):  ワークスペースIDを指定することで対象のワークスペースでアサインされているスケジュールのみを取得できる
                term_start (str):  日付での範囲検索で使用
                term_end (str):  日付での範囲検索で使用

        Returns:
            [Schedule]


        """
        url_path = "/my/schedules"
        http_method = "GET"
        keyword_params: dict[str, Any] = {
            "query_params": query_params,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def get_my_workspace_members(self, query_params: Optional[dict[str, Any]] = None, **kwargs) -> Any:
        """自身のワークスペースメンバー情報一覧を取得する





        Args:
            query_params (dict[str, Any]): Query Parameters
                workspace_id (str):  ワークスペースIDを指定することで対象のワークスペースに所属しているワークスペースメンバー情報のみを取得できる

        Returns:
            [WorkspaceMember]


        """
        url_path = "/my/workspace-members"
        http_method = "GET"
        keyword_params: dict[str, Any] = {
            "query_params": query_params,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def get_my_workspaces(self, **kwargs) -> Any:
        """自身の所属するワークスペース情報一覧を取得する





        Args:

        Returns:
            [Workspace]


        """
        url_path = "/my/workspaces"
        http_method = "GET"
        keyword_params: dict[str, Any] = {}
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def put_my_account(self, request_body: Optional[Any] = None, **kwargs) -> Any:
        """アカウント情報更新





        Args:
            request_body (Any): Request Body
                put_my_account_request (PutMyAccountRequest):  (required)

        Returns:
            Account


        """
        url_path = "/my/account"
        http_method = "PUT"
        keyword_params: dict[str, Any] = {
            "request_body": request_body,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    #########################################
    # Public Method : ScheduleApi
    # NOTE: This method is auto generated by OpenAPI Generator
    #########################################

    def delete_schedule(self, workspace_id: str, schedule_id: str, **kwargs) -> Any:
        """作業計画の削除





        Args:
            workspace_id (str):  ワークスペースID (required)
            schedule_id (str):  スケジュールID (required)

        Returns:
            Schedule


        """
        url_path = f"/workspaces/{workspace_id}/schedules/{schedule_id}"
        http_method = "DELETE"
        keyword_params: dict[str, Any] = {}
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def get_schedule(self, workspace_id: str, schedule_id: str, **kwargs) -> Any:
        """作業計画の取得





        Args:
            workspace_id (str):  ワークスペースID (required)
            schedule_id (str):  スケジュールID (required)

        Returns:
            Schedule


        """
        url_path = f"/workspaces/{workspace_id}/schedules/{schedule_id}"
        http_method = "GET"
        keyword_params: dict[str, Any] = {}
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def get_schedules(self, workspace_id: str, query_params: Optional[dict[str, Any]] = None, **kwargs) -> Any:
        """作業計画の一覧取得





        Args:
            workspace_id (str):  ワークスペースID (required)
            query_params (dict[str, Any]): Query Parameters
                term_start (str):  日付での範囲検索で使用
                term_end (str):  日付での範囲検索で使用
                job_id (str):  ジョブID

        Returns:
            [Schedule]


        """
        url_path = f"/workspaces/{workspace_id}/schedules"
        http_method = "GET"
        keyword_params: dict[str, Any] = {
            "query_params": query_params,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def get_sum_of_schedules(self, workspace_id: str, query_params: Optional[dict[str, Any]] = None, **kwargs) -> Any:
        """ワークスペース全体のスケジュール時間の合計取得





        Args:
            workspace_id (str):  ワークスペースID (required)
            query_params (dict[str, Any]): Query Parameters
                job_id (str):  ジョブID
                includes_archived_job (bool):  アーカイブ化したジョブの合計も含めるかどうか

        Returns:
            SumOfTimes


        """
        url_path = f"/workspaces/{workspace_id}/sum-of-schedules"
        http_method = "GET"
        keyword_params: dict[str, Any] = {
            "query_params": query_params,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def put_schedule(self, workspace_id: str, schedule_id: str, request_body: Optional[Any] = None, **kwargs) -> Any:
        """作業計画の更新





        Args:
            workspace_id (str):  ワークスペースID (required)
            schedule_id (str):  スケジュールID (required)
            request_body (Any): Request Body
                put_schedule_request (PutScheduleRequest):  (required)

        Returns:
            Schedule


        """
        url_path = f"/workspaces/{workspace_id}/schedules/{schedule_id}"
        http_method = "PUT"
        keyword_params: dict[str, Any] = {
            "request_body": request_body,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    #########################################
    # Public Method : WorkspaceApi
    # NOTE: This method is auto generated by OpenAPI Generator
    #########################################

    def get_workspace(self, workspace_id: str, **kwargs) -> Any:
        """ワークスペースの取得





        Args:
            workspace_id (str):  ワークスペースID (required)

        Returns:
            Workspace


        """
        url_path = f"/workspaces/{workspace_id}"
        http_method = "GET"
        keyword_params: dict[str, Any] = {}
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def get_workspace_tag(self, workspace_id: str, workspace_tag_id: str, **kwargs) -> Any:
        """ワークスペースタグの取得





        Args:
            workspace_id (str):  ワークスペースID (required)
            workspace_tag_id (str):  ワークスペースタグID (required)

        Returns:
            WorkspaceTag


        """
        url_path = f"/workspaces/{workspace_id}/tags/{workspace_tag_id}"
        http_method = "GET"
        keyword_params: dict[str, Any] = {}
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def get_workspace_tag_members(self, workspace_id: str, workspace_tag_id: str, **kwargs) -> Any:
        """ワークスペースタグに紐付いているワークスペースメンバーの一覧取得





        Args:
            workspace_id (str):  ワークスペースID (required)
            workspace_tag_id (str):  ワークスペースタグID (required)

        Returns:
            WorkspaceTagMembers


        """
        url_path = f"/workspaces/{workspace_id}/tags/{workspace_tag_id}/members"
        http_method = "GET"
        keyword_params: dict[str, Any] = {}
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def get_workspace_tags(self, workspace_id: str, **kwargs) -> Any:
        """ワークスペースタグ一覧の取得





        Args:
            workspace_id (str):  ワークスペースID (required)

        Returns:
            [WorkspaceTag]


        """
        url_path = f"/workspaces/{workspace_id}/tags"
        http_method = "GET"
        keyword_params: dict[str, Any] = {}
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def put_workspace(self, workspace_id: str, request_body: Optional[Any] = None, **kwargs) -> Any:
        """ワークスペースの更新





        Args:
            workspace_id (str):  ワークスペースID (required)
            request_body (Any): Request Body
                put_workspace_request (PutWorkspaceRequest):  (required)

        Returns:
            Workspace


        """
        url_path = f"/workspaces/{workspace_id}"
        http_method = "PUT"
        keyword_params: dict[str, Any] = {
            "request_body": request_body,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def put_workspace_tag(self, workspace_id: str, workspace_tag_id: str, request_body: Optional[Any] = None, **kwargs) -> Any:
        """ワークスペースタグの更新





        Args:
            workspace_id (str):  ワークスペースID (required)
            workspace_tag_id (str):  ワークスペースタグID (required)
            request_body (Any): Request Body
                put_workspace_tag_request (PutWorkspaceTagRequest):  (required)

        Returns:
            WorkspaceTag


        """
        url_path = f"/workspaces/{workspace_id}/tags/{workspace_tag_id}"
        http_method = "PUT"
        keyword_params: dict[str, Any] = {
            "request_body": request_body,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    #########################################
    # Public Method : WorkspaceMemberApi
    # NOTE: This method is auto generated by OpenAPI Generator
    #########################################

    def delete_workspace_member(self, workspace_id: str, workspace_member_id: str, **kwargs) -> Any:
        """ワークスペースメンバーの削除





        Args:
            workspace_id (str):  ワークスペースID (required)
            workspace_member_id (str):  ワークスペースメンバーID (required)

        Returns:
            WorkspaceMember


        """
        url_path = f"/workspaces/{workspace_id}/members/{workspace_member_id}"
        http_method = "DELETE"
        keyword_params: dict[str, Any] = {}
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def get_workspace_member(self, workspace_id: str, workspace_member_id: str, **kwargs) -> Any:
        """ワークスペースメンバーの取得





        Args:
            workspace_id (str):  ワークスペースID (required)
            workspace_member_id (str):  ワークスペースメンバーID (required)

        Returns:
            WorkspaceMember


        """
        url_path = f"/workspaces/{workspace_id}/members/{workspace_member_id}"
        http_method = "GET"
        keyword_params: dict[str, Any] = {}
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def get_workspace_member_tags(self, workspace_id: str, workspace_member_id: str, **kwargs) -> Any:
        """ワークスペースメンバーのタグ一覧取得





        Args:
            workspace_id (str):  ワークスペースID (required)
            workspace_member_id (str):  ワークスペースメンバーID (required)

        Returns:
            WorkspaceMemberTags


        """
        url_path = f"/workspaces/{workspace_id}/members/{workspace_member_id}/tags"
        http_method = "GET"
        keyword_params: dict[str, Any] = {}
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def get_workspace_members(self, workspace_id: str, query_params: Optional[dict[str, Any]] = None, **kwargs) -> Any:
        """ワークスペースメンバー一覧の取得





        Args:
            workspace_id (str):  ワークスペースID (required)
            query_params (dict[str, Any]): Query Parameters
                sort (str):  sort key(降順にしたい場合は先頭に-(ハイフン)を付ける)
                includes_inactive_members (bool):  無効化したワークスペースメンバーも含めるかどうか

        Returns:
            [WorkspaceMember]


        """
        url_path = f"/workspaces/{workspace_id}/members"
        http_method = "GET"
        keyword_params: dict[str, Any] = {
            "query_params": query_params,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)

    def put_workspace_member(self, workspace_id: str, workspace_member_id: str, request_body: Optional[Any] = None, **kwargs) -> Any:
        """ワークスペースメンバーの変更





        Args:
            workspace_id (str):  ワークスペースID (required)
            workspace_member_id (str):  ワークスペースメンバーID (required)
            request_body (Any): Request Body
                put_workspace_member_request (PutWorkspaceMemberRequest):  (required)

        Returns:
            WorkspaceMember


        """
        url_path = f"/workspaces/{workspace_id}/members/{workspace_member_id}"
        http_method = "PUT"
        keyword_params: dict[str, Any] = {
            "request_body": request_body,
        }
        keyword_params.update(**kwargs)
        return self._request_wrapper(http_method, url_path, **keyword_params)
