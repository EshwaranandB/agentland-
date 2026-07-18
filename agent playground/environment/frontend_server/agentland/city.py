import json

from django.shortcuts import render

from .projection import project_city_frames


def city_page(request, session):
    """Render the Phaser world from persisted AgentLand event frames only."""
    frames = json.dumps(project_city_frames(session)).replace("</", "<\\/")
    return render(request, "agentland/city.html", {"frames_json": frames})
