from __future__ import annotations

from abc import ABC

from pocketbase.models.utils.base_model import BaseModel
from pocketbase.models.utils.list_result import ListResult
from pocketbase.services.utils.base_crud_service import BaseCrudService


class SubCrudService(BaseCrudService, ABC):
    def base_crud_path(self) -> str:
        """Base path for the crud actions (without trailing slash, eg. '/admins')."""

    def get_full_list(
        self,
        sub: str,
        batch: int = 200, 
        expand: str = None,
        filter: str = None,
        sort: str = None,
        query: dict = None,
        headers: dict = None,
    ) -> list[BaseModel]:
        return self._get_full_list(
            self.base_crud_path(sub),
            batch=batch,
            expand=expand,
            filter=filter,
            sort=sort,
            query=query,
            headers=headers,
        )

    def get_list(
        self,
        sub: str,
        page: int = 1, 
        per_page: int = 30,
        expand: str = None,
        filter: str = None,
        sort: str = None,
        query: dict = None,
        headers: dict = None,
    ) -> ListResult:
        return self._get_list(
            self.base_crud_path(sub), 
            page=page,
            per_page=per_page,
            expand=expand,
            filter=filter,
            sort=sort,
            query=query,
            headers=headers,
        )

    def get_one(self, sub: str, id: str, query_params: dict = {}) -> BaseModel:
        return self._get_one(self.base_crud_path(sub), id, query_params)

    def create(
        self, sub: str, body_params: dict = {}, query_params: dict = {}
    ) -> BaseModel:
        return self._create(self.base_crud_path(sub), body_params, query_params)

    def update(
        self, sub: str, id: str, body_params: dict = {}, query_params: dict = {}
    ) -> BaseModel:
        return self._update(self.base_crud_path(sub), id, body_params, query_params)

    def delete(self, sub: str, id: str, query_params: dict = {}) -> bool:
        return self._delete(self.base_crud_path(sub), id, query_params)
