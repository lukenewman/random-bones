import React, { useEffect, useState } from 'react';
import ReactDOM from 'react-dom';
import './index.css';

const App = () => {
  const [ embedURL, setEmbedURL ] = useState("");
  const [ isLoading, setIsLoading ] = useState(true);

  const onButtonClick= () => {
    setIsLoading(true);
  };

  useEffect(() => {
    document.body.style.backgroundColor = "black";
  });

  useEffect(() => {
    async function fetchEpisode() {
      try {
        const res = await fetch('https://l8r73p.deta.dev/episode');
        const json = await res.json();
        const episode = json[0][0];
        setEmbedURL(episode.url.replace('www', 'api') + "embed-html");
        setIsLoading(false);
      } catch(e) {
        console.log(e);
      }
    }
    fetchEpisode();
  }, [ isLoading ]);

  return (
    <div className="app">
      <header>
        <h1>random bones</h1>
      </header>
      <main>
          <embed src={embedURL} />
          <button type="button" className="button" onClick={onButtonClick}>oi oi!</button>
      </main>
      <footer>
        <h4>a project by <a href="https://soundcloud.com/lukenewman">new man</a></h4>
      </footer>
    </div>
  );
}

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
