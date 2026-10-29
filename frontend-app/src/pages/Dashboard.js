import { useEffect, useState } from "react";
import Sidebar from "../components/Sidebar";
import api from "../api/api";

function Dashboard() {
  const [summary, setSummary] = useState({
    total_patients: 0,
    appointments_last_week: 0,
    total_billing: 0,
  });

  const [appointments, setAppointments] = useState([]);

  useEffect(() => {
    const loadSummary = async () => {
      try {
        const response = await api.get("/reports/summary");
        setSummary(response.data);
      } catch (error) {
        console.log(error);
      }
    };

    const loadAppointments = async () => {
      try {
        const response = await api.get("/appointments/");
        setAppointments(response.data);
      } catch (error) {
        console.log(error);
      }
    };

    loadSummary();
    loadAppointments();
  }, []);

  return (
    <div style={{ display: "flex" }}>
      <Sidebar />

      <div style={{ padding: "20px", width: "100%" }}>
        <h1>Digital Healthcare Dashboard</h1>

        {/* Dashboard Cards */}
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(2, 1fr)",
            gap: "20px",
            marginTop: "20px",
          }}
        >
          <div
            style={{
              background: "#f5f5f5",
              padding: "20px",
              borderRadius: "10px",
            }}
          >
            <h3>Total Patients</h3>
            <h1>{summary.total_patients}</h1>
          </div>

          <div
            style={{
              background: "#f5f5f5",
              padding: "20px",
              borderRadius: "10px",
            }}
          >
            <h3>Appointments This Week</h3>
            <h1>{summary.appointments_last_week}</h1>
          </div>

          <div
            style={{
              background: "#f5f5f5",
              padding: "20px",
              borderRadius: "10px",
            }}
          >
            <h3>Total Revenue</h3>
            <h1>R{summary.total_billing}</h1>
          </div>

          <div
            style={{
              background: "#f5f5f5",
              padding: "20px",
              borderRadius: "10px",
            }}
          >
            <h3>System Status</h3>
            <h1>✅ Active</h1>
          </div>
        </div>

        {/* Recent Appointments */}
        <div
          style={{
            marginTop: "30px",
            backgroundColor: "white",
            borderRadius: "12px",
            padding: "20px",
            boxShadow: "0 2px 10px rgba(0,0,0,0.1)",
          }}
        >
          <h2 style={{ marginBottom: "20px" }}>
            Recent Appointments
          </h2>

          <table
            style={{
              width: "100%",
              borderCollapse: "collapse",
            }}
          >
            <thead>
              <tr
                style={{
                  backgroundColor: "#2563eb",
                  color: "white",
                }}
              >
                <th
                  style={{
                    padding: "15px",
                    textAlign: "left",
                  }}
                >
                  Appointment ID
                </th>

                <th
                  style={{
                    padding: "15px",
                    textAlign: "left",
                  }}
                >
                  Patient ID
                </th>

                <th
                  style={{
                    padding: "15px",
                    textAlign: "left",
                  }}
                >
                  Appointment Date
                </th>

                <th
                  style={{
                    padding: "15px",
                    textAlign: "left",
                  }}
                >
                  Status
                </th>
              </tr>
            </thead>

            <tbody>
              {appointments.map((appointment, index) => (
                <tr
                  key={appointment.appointment_id}
                  style={{
                    backgroundColor:
                      index % 2 === 0
                        ? "#f9fafb"
                        : "white",
                  }}
                >
                  <td
                    style={{
                      padding: "15px",
                      borderBottom: "1px solid #e5e7eb",
                    }}
                  >
                    {appointment.appointment_id}
                  </td>

                  <td
                    style={{
                      padding: "15px",
                      borderBottom: "1px solid #e5e7eb",
                    }}
                  >
                    {appointment.patient_id}
                  </td>

                  <td
                    style={{
                      padding: "15px",
                      borderBottom: "1px solid #e5e7eb",
                    }}
                  >
                    {new Date(
                      appointment.appointment_date
                    ).toLocaleString()}
                  </td>

                  <td
                    style={{
                      padding: "15px",
                      borderBottom: "1px solid #e5e7eb",
                    }}
                  >
                    <span
                      style={{
                        backgroundColor:
                          appointment.status ===
                          "Scheduled"
                            ? "#dbeafe"
                            : "#dcfce7",
                        color:
                          appointment.status ===
                          "Scheduled"
                            ? "#1e40af"
                            : "#166534",
                        padding: "6px 12px",
                        borderRadius: "20px",
                        fontWeight: "bold",
                      }}
                    >
                      {appointment.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;