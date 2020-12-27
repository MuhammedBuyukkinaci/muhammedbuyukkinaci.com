using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using mywebsite.Models;

namespace mywebsite.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            int saat = DateTime.Now.Hour;



            return View();
        }

        public IActionResult Contact()
        {
            return View();
        }

        public IActionResult YouKnowMe()
        {
            return View();
        }

        public IActionResult Testimonials()
        {
            return View();
        }

        public IActionResult Photos()
        {
            return View();
        }

        public IActionResult Projects()
        {
            return View();
        }

        public IActionResult MonetaryMetrics()
        {
            return View();
        }






        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
