def generate_recommendations(instance):

    recommendations = []

    instance_type = instance["instance_type"]

    if instance_type == "t3.micro":

        recommendations.append({
            "issue": "Low utilization possible",
            "recommendation": "Stop instance during non-working hours",
            "estimated_savings": "$10/month"
        })

    elif instance_type == "t3.large":

        recommendations.append({
            "issue": "Potential overprovisioning",
            "recommendation": "Downgrade to t3.medium",
            "estimated_savings": "$40/month"
        })

    else:

        recommendations.append({
            "issue": "No major optimization needed",
            "recommendation": "Monitor usage regularly",
            "estimated_savings": "$0"
        })

    return recommendations
