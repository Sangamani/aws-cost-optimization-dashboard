import { useEffect, useState } from "react";
import axios from "axios";

function App() {

  const [instances, setInstances] = useState([]);
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {

    axios
      .get("http://127.0.0.1:8000/instances")
      .then((response) => {
        setInstances(response.data);
      });

    axios
      .get("http://127.0.0.1:8000/recommendations")
      .then((response) => {
        setRecommendations(response.data);
      });

  }, []);

  return (

    <div
      style={{
        padding: "30px",
        fontFamily: "Arial",
        backgroundColor: "#0f172a",
        minHeight: "100vh",
        color: "white"
      }}
    >

      <h1>AI AWS Cost Detective Dashboard</h1>

      <div
        style={{
          display: "flex",
          gap: "20px",
          marginBottom: "30px"
        }}
      >

        <div
          style={{
            border: "1px solid gray",
            padding: "20px",
            borderRadius: "10px",
            width: "200px"
          }}
        >
          <h2>Total Instances</h2>
          <p>{instances.length}</p>
        </div>

        <div
          style={{
            border: "1px solid gray",
            padding: "20px",
            borderRadius: "10px",
            width: "200px"
          }}
        >
          <h2>Running Instances</h2>

          <p>
            {
              instances.filter(
                (instance) => instance.state === "running"
              ).length
            }
          </p>

        </div>

      </div>

      <h2>Live EC2 Instances</h2>

      <table
        border="1"
        cellPadding="10"
        style={{
          borderCollapse: "collapse",
          width: "100%",
          marginBottom: "40px"
        }}
      >

        <thead>
          <tr>
            <th>Instance ID</th>
            <th>Instance Type</th>
            <th>State</th>
          </tr>
        </thead>

        <tbody>

          {instances.map((instance, index) => (

            <tr key={index}>
              <td>{instance.instance_id}</td>
              <td>{instance.instance_type}</td>
              <td>{instance.state}</td>
            </tr>

          ))}

        </tbody>

      </table>

      <h2>AI Recommendations</h2>

      {

        recommendations.map((item, index) => (

          <div
            key={index}
            style={{
              border: "1px solid gray",
              padding: "20px",
              borderRadius: "10px",
              marginBottom: "20px"
            }}
          >

            <h3>{item.instance.instance_id}</h3>

            {

              item.recommendations.map((rec, i) => (

                <div key={i}>

                  <p>
                    <strong>Issue:</strong> {rec.issue}
                  </p>

                  <p>
                    <strong>Recommendation:</strong> {rec.recommendation}
                  </p>

                  <p>
                    <strong>Estimated Savings:</strong> {rec.estimated_savings}
                  </p>

                </div>

              ))

            }

          </div>

        ))

      }

    </div>
  );
}

export default App;
