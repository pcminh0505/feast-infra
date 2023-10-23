import { useEffect } from "react";

const CustomComponent = () => {
  useEffect(() => {
    fetch("http://localhost:8888/projects-list.json", {
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((json) => console.log(json))
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return <div>Different ways to fetch Data Hehehe</div>;
};

export default CustomComponent;
