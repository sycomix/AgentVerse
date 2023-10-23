from __future__ import annotations

import random
from typing import TYPE_CHECKING, Any, List, Union

from . import visibility_registry as VisibilityRegistry
from .base import BaseVisibility

if TYPE_CHECKING:
    from agentverse.environments import BaseEnvironment


@VisibilityRegistry.register("prisoner")
class PrisonerVisibility(BaseVisibility):
    """
    Visibility function for classroom, supports group discussion.

    Args:
        student_per_group:
            The number of students per group.
        num_discussion_turn:
            The number of turns for group discussion.
        grouping:
            The grouping information. If it is a string, then it should be a
            grouping method, options are ["random", "sequential"]. If it is a
            list of list of int, then it should be the grouping information.
    """

    current_turn: int = 0

    def update_visible_agents(self, environment: BaseEnvironment):
        self.update_receiver(environment, reset=False)

    def update_receiver(self, environment: BaseEnvironment, reset=False):
        if reset:
            for agent in environment.agents:
                agent.set_receiver(["all"])

    def reset(self):
        self.current_turn = 0
