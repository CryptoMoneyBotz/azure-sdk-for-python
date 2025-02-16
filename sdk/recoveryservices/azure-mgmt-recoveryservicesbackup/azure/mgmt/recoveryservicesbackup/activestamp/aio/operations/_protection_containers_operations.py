# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._protection_containers_operations import build_get_request, build_inquire_request, build_refresh_request, build_register_request, build_unregister_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ProtectionContainersOperations:
    """ProtectionContainersOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.recoveryservicesbackup.activestamp.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get(
        self,
        vault_name: str,
        resource_group_name: str,
        fabric_name: str,
        container_name: str,
        **kwargs: Any
    ) -> "_models.ProtectionContainerResource":
        """Gets details of the specific container registered to your Recovery Services Vault.

        :param vault_name: The name of the recovery services vault.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present.
        :type resource_group_name: str
        :param fabric_name: Name of the fabric where the container belongs.
        :type fabric_name: str
        :param container_name: Name of the container whose details need to be fetched.
        :type container_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProtectionContainerResource, or the result of cls(response)
        :rtype: ~azure.mgmt.recoveryservicesbackup.activestamp.models.ProtectionContainerResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ProtectionContainerResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            vault_name=vault_name,
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            fabric_name=fabric_name,
            container_name=container_name,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ProtectionContainerResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}'}  # type: ignore


    @distributed_trace_async
    async def register(
        self,
        vault_name: str,
        resource_group_name: str,
        fabric_name: str,
        container_name: str,
        parameters: "_models.ProtectionContainerResource",
        **kwargs: Any
    ) -> Optional["_models.ProtectionContainerResource"]:
        """Registers the container with Recovery Services vault.
        This is an asynchronous operation. To track the operation status, use location header to call
        get latest status of
        the operation.

        :param vault_name: The name of the recovery services vault.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present.
        :type resource_group_name: str
        :param fabric_name: Fabric name associated with the container.
        :type fabric_name: str
        :param container_name: Name of the container to be registered.
        :type container_name: str
        :param parameters: Request body for operation.
        :type parameters:
         ~azure.mgmt.recoveryservicesbackup.activestamp.models.ProtectionContainerResource
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProtectionContainerResource, or the result of cls(response)
        :rtype: ~azure.mgmt.recoveryservicesbackup.activestamp.models.ProtectionContainerResource or
         None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.ProtectionContainerResource"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'ProtectionContainerResource')

        request = build_register_request(
            vault_name=vault_name,
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            fabric_name=fabric_name,
            container_name=container_name,
            content_type=content_type,
            json=_json,
            template_url=self.register.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ProtectionContainerResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    register.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}'}  # type: ignore


    @distributed_trace_async
    async def unregister(
        self,
        vault_name: str,
        resource_group_name: str,
        fabric_name: str,
        container_name: str,
        **kwargs: Any
    ) -> None:
        """Unregisters the given container from your Recovery Services Vault. This is an asynchronous
        operation. To determine
        whether the backend service has finished processing the request, call Get Container Operation
        Result API.

        :param vault_name: The name of the recovery services vault.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present.
        :type resource_group_name: str
        :param fabric_name: Name of the fabric where the container belongs.
        :type fabric_name: str
        :param container_name: Name of the container which needs to be unregistered from the Recovery
         Services Vault.
        :type container_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_unregister_request(
            vault_name=vault_name,
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            fabric_name=fabric_name,
            container_name=container_name,
            template_url=self.unregister.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    unregister.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}'}  # type: ignore


    @distributed_trace_async
    async def inquire(
        self,
        vault_name: str,
        resource_group_name: str,
        fabric_name: str,
        container_name: str,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """Inquires all the protectable items under the given container.

        This is an async operation and the results should be tracked using location header or
        Azure-async-url.

        :param vault_name: The name of the recovery services vault.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present.
        :type resource_group_name: str
        :param fabric_name: Fabric Name associated with the container.
        :type fabric_name: str
        :param container_name: Name of the container in which inquiry needs to be triggered.
        :type container_name: str
        :param filter: OData filter options.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_inquire_request(
            vault_name=vault_name,
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            fabric_name=fabric_name,
            container_name=container_name,
            filter=filter,
            template_url=self.inquire.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    inquire.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/inquire'}  # type: ignore


    @distributed_trace_async
    async def refresh(
        self,
        vault_name: str,
        resource_group_name: str,
        fabric_name: str,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """Discovers all the containers in the subscription that can be backed up to Recovery Services
        Vault. This is an
        asynchronous operation. To know the status of the operation, call GetRefreshOperationResult
        API.

        :param vault_name: The name of the recovery services vault.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present.
        :type resource_group_name: str
        :param fabric_name: Fabric name associated the container.
        :type fabric_name: str
        :param filter: OData filter options.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_refresh_request(
            vault_name=vault_name,
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            fabric_name=fabric_name,
            filter=filter,
            template_url=self.refresh.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    refresh.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/refreshContainers'}  # type: ignore

