import { Link } from "react-router-dom";

function Sidebar() {
  const logout = () => {
    localStorage.removeItem("token");
    window.location.href = "/";
  };

  return (
    <div
      style={{
        width: "250px",
        height: "100vh",
        background: "#2563eb",
        color: "white",
        padding: "20px",
      }}
    >
      <h2>Healthcare System</h2>

      <hr />

      <p>
        <Link
          to="/dashboard"
          style={{
            color: "white",
            textDecoration: "none",
          }}
        >
          Dashboard
        </Link>
      </p>

      <p>
        <Link
          to="/facial-recognition"
          style={{
            color: "white",
            textDecoration: "none",
          }}
        >
          Facial Recognition
        </Link>
      </p>

      <p>
        <Link
          to="/patients"
          style={{
            color: "white",
            textDecoration: "none",
          }}
        >
          Patients
        </Link>
      </p>

      <p>
        <Link
          to="/billing"
          style={{
            color: "white",
            textDecoration: "none",
          }}
        >
          Billing
        </Link>
      </p>

      <p>
        <Link
          to="/medical-records"
          style={{
            color: "white",
            textDecoration: "none",
          }}
        >
          Medical Records
        </Link>
      </p>

      <p>
        <Link
          to="/appointments"
          style={{
            color: "white",
            textDecoration: "none",
          }}
        >
          Appointments
        </Link>
      </p>

      <button
        onClick={logout}
        style={{
          marginTop: "20px",
          width: "100%",
          padding: "10px",
          background: "#dc2626",
          color: "white",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer",
        }}
      >
        Logout
      </button>
    </div>
  );
}

export default Sidebar;