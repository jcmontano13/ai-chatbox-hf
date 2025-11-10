from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services.local_hf import generate_reply

@api_view(["POST"])
def chat(request):
    message = (request.data.get("message") or "").strip()
    if not message:
        return Response({"error": "message is required"}, status=400)

    try:
        reply = generate_reply(message, max_length=80)
        # Basic fallback if the model mirrors the prompt
        if not reply:
            reply = "I’m thinking about that. Could you say it another way?"
        return Response({"reply": reply})
    except Exception as e:
        return Response({"error": str(e)}, status=500)