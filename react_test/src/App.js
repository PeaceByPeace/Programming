// import logo from './logo.svg';
// import './App.css';
import Home from "./pages/Home"
import Rooms from "./pages/Rooms"
import SingleRoom from "./pages/SingleRoom"
import Error from "./pages/Error"
import {Route, Routes} from 'react-router-dom'

function App() {
  return (
    <div>
        <Routes>
          <Route path="/" element={<Home></Home>}></Route>
          <Route path="/rooms/" element={<Rooms></Rooms>}></Route>
          <Route path="/rooms/:id" element={<SingleRoom></SingleRoom>}></Route>
          <Route path="*" element={<Error></Error>}></Route>
        </Routes>

    </div>

  );
}

export default App;
