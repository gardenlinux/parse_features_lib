import pytest
import os
from python_gardenlinux_lib.oras.registry import GlociRegistry, setup_registry

CONTAINER_NAME_ZOT_EXAMPLE = "127.0.0.1:18081/gardenlinux-example"
GARDENLINUX_ROOT_DIR_EXAMPLE = "test-data/gardenlinux/"


@pytest.mark.usefixtures("zot_session")
@pytest.mark.parametrize(
    "version, cname, arch",
    [
        ("today", "aws-gardener_prod", "arm64"),
        ("today", "aws-gardener_prod", "amd64"),
        ("today", "gcp-gardener_prod", "arm64"),
        ("today", "gcp-gardener_prod", "amd64"),
        ("today", "azure-gardener_prod", "arm64"),
        ("today", "azure-gardener_prod", "amd64"),
        ("today", "openstack-gardener_prod", "arm64"),
        ("today", "openstack-gardener_prod", "amd64"),
        ("today", "openstackbaremetal-gardener_prod", "arm64"),
        ("today", "openstackbaremetal-gardener_prod", "amd64"),
        ("today", "metal-kvm_dev", "arm64"),
        ("today", "metal-kvm_dev", "amd64"),
    ],
)
def test_push_example(version, cname, arch):

    container_name = f"{CONTAINER_NAME_ZOT_EXAMPLE}:{version}"
    registry = setup_registry(
        container_name,
        insecure=True,
        private_key="cert/oci-sign.key",
        public_key="cert/oci-sign.crt",
    )
    registry.push_image_manifest(
        arch,
        cname,
        version,
        GARDENLINUX_ROOT_DIR_EXAMPLE,
        f"{GARDENLINUX_ROOT_DIR_EXAMPLE}/.build",
    )
