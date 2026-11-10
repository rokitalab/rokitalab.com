/*
  opens external links in a new tab.
*/

{
  const onLoad = () => {
    const links = document.querySelectorAll("a[href]");
    for (const link of links) {
      if (link.protocol !== "http:" && link.protocol !== "https:") continue;
      if (link.hostname === window.location.hostname) continue;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
    }
  };

  // after page loads
  window.addEventListener("load", onLoad);
}
