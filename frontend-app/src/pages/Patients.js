import { useState } from "react";
import Sidebar from "../components/Sidebar";
import api from "../api/api";

function Patients() {
  const [patientId, setPatientId] = useState("");
  const [patient, setPatient] = useState(null);

  // Add Patient states
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");

  // Search Patient
  const getPatient = async () => {
    try {
      const response = await api.get(
        `/patients/${patientId}`
      );

      setPatient(response.data);
    } catch (error) {
      alert("Patient not found");
      console.log(error);
    }
  };

  // Create Patient
  const createPatient = async () => {
    try {
      const response = await api.post("/patients/", {
        name,
        phone,
      });

      alert("Patient created successfully");

      console.log(response.data);

      setName("");
      setPhone("");
    } catch (error) {
      console.log(error);
      alert("Failed to create patient");
    }
  };

  return (
    <div style={{ display: "flex" }}>
      <Sidebar />

      <div style={{ padding: "20px", width: "100%" }}>
        <h1>Patients</h1>

        {/* Search Patient */}
        <h2>Search Patient</h2>

        <input
          type="number"
          placeholder="Enter Patient ID"
          value={patientId}
          onChange={(e) =>
            setPatientId(e.target.value)
          }
        />

        <button
          onClick={getPatient}
          style={{ marginLeft: "10px" }}
        >
          Search
        </button>

        {/* Patient Details */}
        {patient && (
          <div
            style={{
              marginTop: "20px",
              padding: "20px",
              border: "1px solid #ddd",
            }}
          >
            <h3>Patient Details</h3>

            <pre>
              {JSON.stringify(
                patient,
                null,
                2
              )}
            </pre>
          </div>
        )}

        {/* Add Patient */}
        <h2 style={{ marginTop: "30px" }}>
          Add Patient
        </h2>

        <input
          type="text"
          placeholder="Patient Name"
          value={name}
          onChange={(e) =>
            setName(e.target.value)
          }
          style={{
            display: "block",
            marginBottom: "10px",
            padding: "10px",
            width: "300px",
          }}
        />

        <input
          type="text"
          placeholder="Phone Number"
          value={phone}
          onChange={(e) =>
            setPhone(e.target.value)
          }
          style={{
            display: "block",
            marginBottom: "10px",
            padding: "10px",
            width: "300px",
          }}
        />

        <button
          onClick={createPatient}
          style={{
            padding: "10px 20px",
            background: "#2563eb",
            color: "white",
            border: "none",
          }}
        >
          Create Patient
        </button>
      </div>
    </div>
  );
}

export default Patients;