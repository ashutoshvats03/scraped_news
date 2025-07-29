"use client";
import axios from 'axios';
import { useEffect, useRef, useState } from 'react';
function App() {

  const ref = useRef([]);
  const [news, setnews] = useState([]);


  useEffect(() => {
    const fetchData = async () => {
      const Response = await axios.get('http://127.0.0.1:8000/get_news/')
      const { data } = Response
      if (Response.status == 200) {
        console.log(data.news_list)
        console.log(news)
        console.log("success")
        setnews(data.news_list)
      }
      else {
        console.log(Response)
      }
    }
    fetchData()
  }, [])


  useEffect(() => {
    const options = {
      root: null,

      threshold: 0.4, // Multiple thresholds for better detection
    };
    const callback = (entries) => {
      entries.forEach((entry) => {
        const a = entry.intersectionRect.height
        const b = entry.boundingClientRect.height
        const ratio = b / (a || 1); // prevent divide by zero

        // Clamp ratio between 0 and 1
        const opacity = Math.max(0.2, Math.min(1, ratio));

        entry.target.style.opacity = entry.isIntersecting ? opacity : 0.1;
      })
      console.log(entries)
    }
    const observer = new IntersectionObserver(callback, options)
    ref.current.forEach((element) => {
      observer.observe(element)
    })
  }, [news])


  return (
    // Main container for the entire application, setting dark theme and full screen height
    <div className='bg-black'>
      <div className="max-h-[90vh] max-w-[60%] bg-black text-gray-100 font-inter flex flex-col m-auto">
        {/* News content display area */}
        <div className="flex-grow flex items-center justify-center p-4">
          <div >
            {ref.current = []}
            {news.map((currentNews, index) => {
              return (
                <div
                  ref={(el) => ref.current[index] = el}
                  key={currentNews.news_id}
                  className="bg-neutral-300  rounded-xl shadow-lg mb-8 max-w-2xl w-full h-[80vh] flex flex-col overflow-auto md:p-10 lg:p-12 transition-opacity duration-500 ease-in-out"
                >

                  {/* News Title */}
                  <a
                    target="_blank"
                    href={currentNews.link}
                  >
                    <h1 className="text-2xl md:text-3xl font-bold text-black mb-4 leading-tight">
                      {currentNews.title}
                    </h1>
                  </a>

                  {/* Author and Published Date */}
                  <div className="text-sm text-gray-700 mb-6 flex flex-wrap gap-x-4">
                    <span>By: {currentNews.author.replace(/\[|\]|'/g, '')}</span> {/* Clean up author string */}
                    <span>Published: {currentNews.published}</span>
                  </div>
                  {/* News Content */}
                  <p className="text-sm font-bold md:text-md text-black leading-relaxed flex-grow">
                    {currentNews.summary}
                  </p>
                </div>
              )
            })}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
