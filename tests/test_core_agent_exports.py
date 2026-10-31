"""Tests for public exports of vanna.core.agent."""

import pytest


def test_audit_config_importable_from_core_agent():
    from vanna.core.agent import AgentConfig, AuditConfig

    audit_config = AuditConfig(include_full_ai_responses=True)
    agent_config = AgentConfig(audit_config=audit_config)

    assert agent_config.audit_config.include_full_ai_responses is True


def test_audit_config_importable_from_core_agent_module_all():
    from vanna.core import agent

    assert "AuditConfig" in agent.__all__
