import React, { useEffect } from "react";
import { useAuth } from "./providers/authProvider";
import { refreshFetch } from "./api";
import { goToLogin } from "./routes/navigation";
import Routes from "./routes/Routes";
import GridLoader from "react-spinners/GridLoader";


// TODO: do an accessibility audit

function App() {
  const { loading: isLoading, setLoading: setIsLoading, setToken } = useAuth();

  // TODO: apply to requests other than refresh
  // checks specifically to see if the token had become corrupted
  async function checkResponse(res) {
    if (res.status === 422) {
      const error = await res.json();
      if (error.msg === "Signature verification failed") {
        goToLogin();
      }
    }
    return res;
  }

  useEffect(() => {
    setIsLoading(true);
    const fetchRefresh = async () => {
      const res = await refreshFetch();
      checkResponse(res);
      if (res.ok) {
        const tokenJSON = await res.json();
        setToken(tokenJSON);
      } else {
        setToken(null);
      }
      setIsLoading(false);
    };

    fetchRefresh();
  }, []);

  if (isLoading) return <GridLoader />;

  return (
    <div>
      <main>
        <Routes />
      </main>
    </div>
  );
}

export default App;
