/*
  show back-to-top button after scrolling down.
*/

{
  const onScroll = () => {
    const button = document.querySelector(".back-to-top");
    if (button) button.dataset.show = window.scrollY > 400;
  };

  // after page loads and when user scrolls
  window.addEventListener("load", onScroll);
  window.addEventListener("scroll", onScroll, { passive: true });
}
