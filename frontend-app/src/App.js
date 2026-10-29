import { Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import ProtectedRoute from "./components/ProtectedRoute";
import Patients from "./pages/Patients";
import MedicalRecords from "./pages/MedicalRecords";
import FacialRecognition from "./pages/FacialRecognition";

function App() {
  return (
    <Routes>
      <Route
        path="/"
        element={<Login />}
      />

      <Route
        path="/dashboard"
        element={
          <ProtectedRoute>
            <Dashboard />
          </ProtectedRoute>
        }
      />

      <Route
        path="/patients"
        element={
          <ProtectedRoute>
            <Patients />
          </ProtectedRoute>
        }
      />
      <Route
        path="/medical-records"
        element={
          <ProtectedRoute>
            <MedicalRecords />
          </ProtectedRoute>
        }
      />
      <Route
        path="/facial-recognition"
        element={
          <ProtectedRoute>
            <FacialRecognition />
          </ProtectedRoute>
        }
      />
    </Routes>
    
  );
}

export default App;