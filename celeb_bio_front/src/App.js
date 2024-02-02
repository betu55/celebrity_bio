import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import LandingPage from "./LandingPage";
import NotFound from "./NotFound";
import Movies from "./pages/Movies";
import DetailsPage from "./pages/DetailsPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<LandingPage />} />
        <Route path="/movies" element={<Movies />} />
        <Route path="/details" element={<DetailsPage />} />
        <Route element={<NotFound />} />
      </Routes>
    </Router>
  );
}

export default App;
