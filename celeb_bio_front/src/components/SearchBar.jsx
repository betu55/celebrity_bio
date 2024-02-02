import { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

export default function SearchBar({ toParent }) {
  const [keyword, setKeyword] = useState("");
  const [celebData, setCelebData] = useState();
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  // this will send the data from our input field to our backend
  const search = async (key) => {
    try {
      setLoading(true);
      const response = await axios.get("http://localhost:8000/api/search", {
        params: { key },
      });
      setCelebData(response.data);
    } catch (error) {
      console.error("error: ", error);
    } finally {
      setLoading(false);
      navigate("/details", { state: { celebData } });
    }
  };

  // using useEffect becuase we want to send data after celebData has been set.
  useEffect(() => {
    toParent(celebData);
  });
  // this function will set our keyword and reset the searchbars text to empty
  const getSearchData = (e) => {
    if (e.key === "Enter") {
      setKeyword(e.target.value);
      search(keyword); // calling the search function that handles the post re
      e.target.value = "";
      // window.alert(`You typed in: ${keyword}`);

      try {
      } catch (error) {
        console.error("Error:", error);
      }
    }
  };

  return (
    <div className="grid grid-cols-5">
      <input
        onChange={(e) => {
          setKeyword(e.target.value);
        }}
        className="search-bar"
        placeholder="Search Celeb Name..."
        onKeyUp={getSearchData} //invokes the keyHandler() function
      />
    </div>
  );
}
