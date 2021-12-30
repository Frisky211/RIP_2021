import { BrowserRouter, Routes, Route} from "react-router-dom";
import MainPage from "./pages/MainPage";
import PhoneListPage from "./pages/PhoneListPage";
import PhoneDetailPage from "./pages/PhoneDetailPage";

function App() {

  return (
      <BrowserRouter basename="/">
        <Routes>
          <Route path="/" element={<MainPage/>}/>
          <Route path="/phones" element={<PhoneListPage/>}/>
          <Route path="/phones/:pk" element={<PhoneDetailPage/>}/>
        </Routes>
      </BrowserRouter>
  );
}
export default App;
