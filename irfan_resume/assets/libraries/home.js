// below
window.onload = function () {
    $(".first-name").css({
        "opacity": "0",
        "left": "50%"
    });

    $(".last-name").css({
        "opacity": "0",
        "left": "-40%"
    });

    setTimeout(function () {
        $(".loading-screen").css({
            "opacity": "0",
            "transition": "0.3s"
        });

        setTimeout(function () {
            $(".loading-screen").css("display", "none");
            $(".tagline-container").hide();
            $(".count").css("opacity", "0");

            var options = {
                strings: ["", "Enthusiastic Coder", "Android Developer", "Opportunity Seeker", "Web Developer", "Creative Designer"],
                typeSpeed: 40,
                backSpeed: 30,
                backDelay: 300,
                startDelay: 0,
                loop: true,
                showCursor: false,
                loopCount: Infinity,
                onLastStringBackspaced: (self) => {
                    $(".tagline-container").hide();
                },
                preStringTyped: (arrayPos, self) => {
                    if (arrayPos == 1) {
                        //                alert("trigger 1");
                        $(".tagline-container").show();
                    }
                }
            }


            var leftTargetFirstName = "-10%";
            var leftTargetLastName = "20%";
            if ($(window).width() > 480) {
                leftTargetFirstName = "-60%";
                leftTargetLastName = "30%";
            }

            setTimeout(function () {
                $(".first-name").animate({
                    "opacity": "1",
                    "left": leftTargetFirstName
                }, 1000);


                $(".last-name").animate({
                    "opacity": "1",
                    "left": leftTargetLastName
                }, 1000);

                var typed = new Typed(".tagline", options);

            }, 0);

        }, 300);

    }, 600);
};

var alreadyCounted = false;
var alreadyRevealedServices = false;
var alreadyRevealedProjects = false;
var alreadyRevealedAchievements = false;
var alreadyRevealedContact = false;
var alreadyRevealedSkills = false;
var isProjectExpanded = false;
var projectExpanded = $(".project-expanded");
var icon = projectExpanded.find(".icon");
var cover = projectExpanded.find(".cover");
var btnGoto = projectExpanded.find(".btn-goto");
var title = projectExpanded.find(".title");
var category = projectExpanded.find(".category");
var desc = projectExpanded.find(".desc");
var keywords = projectExpanded.find(".keywords");
var close = projectExpanded.find(".close");
var projectContainer = projectExpanded.find(".project-container");
var bg = projectExpanded.find(".bg");
var blurred = projectExpanded.find(".blurred");
var tint = projectExpanded.find(".tint");
var ht = $(window).height() - 190;
var marginTop = 0.05 * ht;
var height = ht - 100 - marginTop;

var collapseNavBar = function () {
    $(".navbar").addClass("top-nav-collapse");
    $(".navbar-brand").addClass("col-lg-6");
    $(".navbar-brand").addClass("col-md-12");
    $(".navbar-brand").addClass("col-sm-6");
    $(".navbar-brand").addClass("col-12");
    $(".navbar-brand").addClass("img-thumb");
    $(".nav-link").addClass("text-light");
};

var expandNavBar = function () {
    $(".navbar").removeClass("top-nav-collapse");
    $(".navbar-brand").removeClass("img-thumb");
    $(".navbar-brand").removeClass("col-lg-6");
    $(".navbar-brand").removeClass("col-md-12");
    $(".navbar-brand").removeClass("col-sm-6");
    $(".navbar-brand").removeClass("col-12");
    $(".nav-link").removeClass("text-light");
};

var setActive = function (anchor) {
    $(".navbar .active").removeClass("active");
    anchor.parent().addClass("active");
};

var loadData = function (project, projectExpanded) {
    var title = project.find(".project__title a").html();
    var category = project.find(".project__category a").html();
    var iconSrc = project.find(".project-content .icon").html();
    var coverSrc = project.find(".project__image img").attr("src");
    var desc = project.find(".project-content .desc").html();
    var keywords = project.find(".project-content .keywords").html();
    var urlToProject = project.find(".project-content .url").html();
    var urlToImage = "url('" + coverSrc + "')";
    //        console.log("title : " + title);
    //        console.log("catergory :" + category);
    //        console.log("iconSrc :" + iconSrc);
    //        console.log("coverSrc :" + coverSrc);
    //        console.log("desc :" + desc);
    //        console.log("keywords :" + keywords);

    projectExpanded.find(".title h4").html(title);
    projectExpanded.find(".category span").html(category);
    projectExpanded.find(".icon img").attr("src", iconSrc);
    projectExpanded.find(".cover img").attr("src", coverSrc);
    projectExpanded.find(".desc p").html(desc);
    projectExpanded.find(".keywords p").html(keywords);
    projectExpanded.find(".btn-goto button a").attr("href", urlToProject);
    projectExpanded.find(".blurred").css({
        "background": urlToImage,
        "background-repeat": "no-repeat",
        "background-size": "cover",
        "background-position": "bottom right"
    });


};

var setInitialPosition = function () {

    projectExpanded.css({
        "opacity": "1"
    });

    cover.css({
        "left": "-20%",
        "opacity": "0",
        "width": "0",
        "height": "0",
        "transition": "0.5s"
    });

    icon.css({
        "top": "150px",
        "left": "150px",
        "opacity": "0"
    });

    bg.css({
        "left": "30%",
        "width": "0",
        "height": height,
        "margin-top": marginTop,
        "opacity": "0.7"
    });

    title.css({
        "left": "40%",
        "opacity": "0"
    });

    category.css({
        "left": "40%",
        "opacity": "0"
    });

    desc.css({
        "top": "290px",
        "opacity": "0",
    });

    keywords.css({
        "bottom": "150px",
        "opacity": "0",
    });

    btnGoto.css({
        "width": "0",
        "height": "0",
        "opacity": "0"
    });

    close.css({
        "opacity": "0",
        "top": "60px",
        "transition": "0.3s"
    });
}

var revealProjectExpanded = function (projectExpanded) {
    projectExpanded.css("display", "block");

    if ($(window).width() < 480) {
        icon.css({
            "top": "-10%",
            "left": "-10%",
            "opacity": "0",
            "transition": "0.8s"
        });
        cover.css({
            "left": "50%",
            "opacity": "0",
            "transition": "0.5s"
        });
        btnGoto.css({
            "transform": "scale(0,0) translateY(-50%)",
            "opacity": "1",
            "transition": "transform 0.3s"
        });
        title.css({
            "left": "50%",
            "opacity": "0",
            "transition": "0.5s"
        });
        category.css({
            "left": "50%",
            "opacity": "0",
            "transition": "0.5s"
        });
        desc.css({
            "top": "100%",
            "opacity": "0",
            "transition": "0.5s"
        });
        keywords.css({
            "bottom": "-10%",
            "opacity": "0",
            "transition": "0.5s"
        });
        close.css({
            "opacity": "0",
            "transition": "0.2s"
        });
        projectContainer.css({
            "box-shadow": "none",
            "transition": "0.8s"
        });

        blurred.css({
            "top": "-110%",
            "transform": "translate(-50%,-50%) scale(1)",
            "transition": "0.5s",
            "opacity": "0"
        });

        tint.css({
            "bottom": "-100",
            "opacity": "0",
            "transition": "0.5s"
        });

        icon.css({
            "top": "0",
            "left": "0",
            "opacity": "1"
        });

        setTimeout(function () {
            cover.css({
                "left": "0%",
                "opacity": "1"
            });
        }, 100);

        setTimeout(function () {
            blurred.css({
                "top": "50%",
                "transform": "translate(-50%,-50%) scale(2)",
                "opacity": "1"
            });
            tint.css({
                "bottom": "0%",
                "opacity": "1"
            })
        }, 200);

        setTimeout(function () {
            btnGoto.css({
                "transform": "scale(1,1) translateY(-50%)",
                "opacity": "1"
            });
        }, 300);

        setTimeout(function () {
            title.css({
                "left": "15px",
                "opacity": "1"
            });
        }, 200);

        setTimeout(function () {
            category.css({
                "left": "15px",
                "opacity": "1"
            });
        }, 300);

        setTimeout(function () {
            desc.css({
                "top": "50%",
                "opacity": "1"
            });
        }, 200);

        setTimeout(function () {
            keywords.css({
                "bottom": "0%",
                "opacity": "1"
            });
        }, 300);

        setTimeout(function () {
            close.css({
                "opacity": "1"
            });
        }, 600);

        setTimeout(function () {
            projectContainer.css({
                "box-shadow": "0px 0px 1000px 10px rgba(0, 0, 0, 0.9)"
            });
        }, 600);
    } else {
        // FOR LARGER SCREENS

        cover.css({
            "left": "0%",
            "opacity": "1",
            "width": "50%",
            "height": "100%"
        });

        setTimeout(function () {
            icon.css({
                "transition": "0.5s",
                "top": "10px",
                "left": "10px",
                "opacity": "1"
            });
        }, 500);

        setTimeout(function () {
            bg.css({
                "transition": "0.5s",
                "left": "49%",
                "width": "51%",
                "opacity": "1"
            });
        }, 200);

        setTimeout(function () {
            title.css({
                "transition": "0.5s",
                "left": "50%",
                "opacity": "1"
            });
        }, 600);

        setTimeout(function () {
            category.css({
                "transition": "0.5s",
                "left": "50%",
                "opacity": "1"
            });
        }, 500);

        setTimeout(function () {
            desc.css({
                "transition": "0.5s",
                "top": "180px",
                "opacity": "1"
            })
        }, 700);

        setTimeout(function () {
            keywords.css({
                "bottom": "50px",
                "opacity": "1",
                "transition": "0.5s"
            });
        }, 900);

        setTimeout(function () {
            btnGoto.css({
                "width": "100px",
                "height": "100px",
                "opacity": "1",
                "transition": "0.3s"
            });
            close.css({
                "opacity": "1",
                "top": "0",
                "transition": "0.3s"
            });
        }, 1100);
    }

    isProjectExpanded = true;
};

var dismissProjectExpanded = function (projectExpanded) {


    if ($(window).width() < 480) {

        projectContainer.css({
            "box-shadow": "none",
            "transition": "0.8s"
        });
        setTimeout(function () {
            icon.css({
                "transition": "1s",
                "top": "-20%",
                "left": "-20%"
            });

            cover.css({
                "transition": "0.5s",
                "left": "50%",
                "opacity": "0"
            });

            blurred.css({
                "top": "-110%",
                "transform": "translate(-50%,-50%) scale(1)",
                "transition": "0.5s",
                "opacity": "0"
            });

            tint.css({
                "bottom": "-100",
                "opacity": "0",
                "transition": "0.5s"
            });

            btnGoto.css({
                "transform": "scale(0,0) translateY(-50%)",
                "opacity": "1",
                "transition": "transform 0.3s"
            });

            title.css({
                "transition": "0.5s",
                "left": "50%",
                "opacity": "0"
            });

            category.css({
                "transition": "0.5s",
                "left": "50%",
                "opacity": "0"
            });

            desc.css({
                "transition": "0.5s",
                "top": "100%",
                "opacity": "0"
            });

            keywords.css({
                "transition": "0.5s",
                "bottom": "-10%",
                "opacity": "0"
            });

            close.css({
                "transition": "0.5s",
                "opacity": "0"
            });

            setTimeout(function () {
                projectExpanded.css({
                    "display": "none"
                });
                isProjectExpanded = false;
            }, 500);

        }, 200);
    } else {
        // For Larger Screens
        setTimeout(function () {
            btnGoto.css({
                "width": "0px",
                "height": "0px",
                "opacity": "0",
                "transition": "0.3s"
            });
            close.css({
                "opacity": "0",
                "top": "60px",
                "transition": "0.3s"
            });
        }, 0);

        setTimeout(function () {
            keywords.css({
                "bottom": "150px",
                "opacity": "0",
                "transition": "0.5s"
            });
        }, 50);

        setTimeout(function () {
            desc.css({
                "transition": "0.5s",
                "top": "290px",
                "opacity": "0"
            })
        }, 100);

        setTimeout(function () {
            category.css({
                "transition": "0.5s",
                "left": "50%",
                "opacity": "0"
            });
        }, 150);

        setTimeout(function () {
            title.css({
                "transition": "0.5s",
                "left": "50%",
                "opacity": "0"
            });
        }, 600);

        setTimeout(function () {
            bg.css({
                "left": "30%",
                "width": "0",
                "height": height,
                "margin-top": marginTop,
                "opacity": "0"
            });
        }, 700);

        setTimeout(function () {
            cover.css({
                "left": "-50%",
                "opacity": "0",
                "transition": "0.5s"
            });
        }, 900);

        setTimeout(function () {
            icon.css({
                "left": "-150px",
                "opacity": "0"
            });
        }, 800);

        setTimeout(function () {
            projectExpanded.css({
                "opacity": "0",
                "transition": "0.3s"
            });
        }, 1200);
        setTimeout(function () {
            projectExpanded.css({
                "display": "none"
            });
            setInitialPosition();
            isProjectExpanded = false;
        }, 1600);
    }
};

$(document).ready(function () {

    $(".scroll-progress").hide();

    particlesJS.load('home', '../assets/others/particles.json', function () {
        //        console.log('callback - particles.js config loaded');
    });

    $(".services-heading, .projects-heading, .achievements-heading, .contact-heading").css({
        "opacity": "0",
        "top": "-80px"
    });

    $(".nav-link").click(function () {
        var anchor = $(this);
        setActive(anchor);
        $(".navbar-collapse").collapse("hide");
    });

    $(".navbar-toggler").click(function () {
        //    collapseNavBar();
    })

    $(".scroll-down-button").click(function () {
        $("html, body").animate({
            scrollTop: $("#about").offset().top
        });
    })

    if ($(window).width() < 768) {
        $(".services-carousel .owl-carousel").owlCarousel({
            loop: true,
            margin: 10,
            autoplay: true,
            slideBy: 1,
            autoplayTimeout: 2500,
            autoplayHoverPause: true,
            responsiveClass: true,
            nav: false,
            responsive: {
                0: {
                    items: 1
                }
            }

        });
    } else if ($(window).width() < 1024) {
        $(".services-carousel .owl-carousel").owlCarousel({
            loop: true,
            margin: 10,
            autoplay: true,
            slideBy: 1,
            autoplayTimeout: 2500,
            autoplayHoverPause: true,
            responsiveClass: true,
            nav: false,
            responsive: {
                0: {
                    items: 2
                }
            }
        });
    } else {
        $(".services-carousel .owl-carousel").owlCarousel({
            loop: true,
            margin: 10,
            autoplay: true,
            slideBy: 1,
            autoplayTimeout: 2500,
            autoplayHoverPause: true,
            responsiveClass: true,
            nav: false,
            responsive: {
                0: {
                    items: 3
                }
            }
        });
    }

    $(".achievements-carousel .owl-carousel").owlCarousel({
        loop: true,
        margin: 10,
        autoplay: true,
        slideBy: 1,
        autoplayTimeout: 2500,
        autoplayHoverPause: true,
        responsiveClass: true,
        nav: false,
        responsive: {
            0: {
                items: 1
            }
        }

    });

    $(".project").hover3d({
        selector: ".project__card",
        shine: true,
        perspective: 2000,
        sensitivity: 8
    });

    projectExpanded.css("display", "none");

    if ($(window).width >= 480) {
        setInitialPosition();
    }

    $(".project").each(function (index, value) {
        $(this).click(function () {
            if (!isProjectExpanded) {
                loadData($(this), projectExpanded);
                revealProjectExpanded(projectExpanded);
            }
        })
    });

    $(".project-expanded").click(function () {
        if (isProjectExpanded) {
            dismissProjectExpanded(projectExpanded);
        }
    });


    $('body').backDetect(function (event) {
        // Callback function
        alert("Look forward to the future, not the past!");
        if (isProjectExpanded) {
            dismissProjectExpanded(projectExpanded);
            event.preventDefault();
        }
    });

    $(".progress-bar").each(function (index, value) {
        $(this).css("width", "0");
    });

});


$(window).on('popstate', function (event) {
    if (isProjectExpanded) {
        projectExpanded.css("display", "none");
        isProjectExpanded = false;
    }
});

$(document).scroll(function () {
    if ($('.navbar').offset().top > 50) {
        collapseNavBar();
        $(".scroll-progress").show();
        var bottom = $("#footer").position().top + $("#footer").height() - $(window).height();
        var widthValue = ($(window).scrollTop()) / bottom * 100;
        if (widthValue > 100) {
            widthValue = 100;
        }
        $(".scroll-progress").css("width", widthValue + "%")
    } else {
        expandNavBar();
        $(".scroll-progress").hide();
    }


    var scrollPos = $(document).scrollTop();
    var aboutPos = $("#about").position().top;
    var servicesPos = $("#services").position().top;
    var projectsPos = $("#projects").position().top;
    var achievementsPos = $("#achievements").position().top;
    var contactPos = $("#contact").position().top;
    var navHome = $(".nav-item a[href='#home']");
    var navAbout = $("a[href='#about']");
    var navServices = $("a[href='#services']");
    var navProjects = $("a[href='#projects']");
    var navAchievements = $("a[href='#achievements']");
    var navContact = $("a[href='#contact']");
    var halfScr = aboutPos / 2;

    if (scrollPos > (aboutPos - halfScr)) {
        $(".scroll-down-button").hide();
    } else {
        $(".scroll-down-button").show();
    }

    if (!alreadyCounted && scrollPos >= ($("#services-counter-bg").position().top - (halfScr * 1.75))) {
        $(".count").css("opacity", "1");
        $('.count').each(function () {
            $(this).prop('Counter', 0).animate({
                Counter: $(this).text()
            }, {
                duration: 4000,
                easing: 'swing',
                step: function (now) {
                    $(this).text(Math.ceil(now));
                }
            });
        });
        alreadyCounted = true;
    }

    if (!alreadyRevealedServices && scrollPos >= ($(".services-heading").position().top - (halfScr * 1.65))) {
        $(".services-heading").animate({
            "opacity": "1",
            "top": "0px"
        }, 1000);
        alreadyRevealedServices = true;
    }

    if (!alreadyRevealedProjects && scrollPos >= ($(".projects-heading").position().top - (halfScr * 1.65))) {
        $(".projects-heading").animate({
            "opacity": "1",
            "top": "0px"
        }, 1000);
        alreadyRevealedProjects = true;
    }

    if (!alreadyRevealedAchievements && scrollPos >= ($(".achievements-heading").offset().top - (halfScr * 1.65))) {
        $(".achievements-heading").animate({
            "opacity": "1",
            "top": "0px"
        }, 1000);
        alreadyRevealedAchievements = true;
    }

    if (!alreadyRevealedContact && scrollPos >= ($(".contact-heading").offset().top - (halfScr * 1.65))) {
        $(".contact-heading").animate({
            "opacity": "1",
            "top": "0px"
        }, 1000);
        alreadyRevealedContact = true;
    }

    //    console.log("scrollPos : " + scrollPos + " ; project : " + ($(".projects-gallery .item").position().top - halfScr));
    //    if (scrollPos >= ($(".projects-gallery .item").position().top - halfScr)) {
    //        console.log("trigger : ");
    //    } else {
    //        console.log("sink : " );
    //    }

    $(".projects-gallery .item .project").each(function (index, value) {
        if (scrollPos >= ($(this).parent().position().top - (halfScr * 1.5))) {
            //            console.log("trigger : " + index);
            $(this).addClass("project-active");
        } else {
            //            console.log("sink : " + index);
            $(this).removeClass("project-active");
        }
    });

    var anchor = $(".about-skills").position().top - halfScr;
    if ($(window).width() >= 480) {
        anchor = aboutPos - halfScr;
    }

    if (!alreadyRevealedSkills && scrollPos >= anchor) {
        //        alert("Hi");
        $(".progress-bar").each(function (index, value) {
            var widthVal = $(this).attr("title");
            //            console.log(widthVal);
            $(this).css({
                "transition": "0.5s",
                "width": widthVal
            });
        });
        alreadyRevealedSkills = true;
    }

    if (scrollPos == 0) {
        $(".navbar .active").removeClass("active");
    } else if (scrollPos > 0 && scrollPos < (aboutPos - halfScr)) {
        setActive(navHome);
    } else if (scrollPos >= aboutPos && scrollPos < (servicesPos - halfScr)) {
        setActive(navAbout);
    } else if (scrollPos >= servicesPos && scrollPos < (projectsPos - halfScr)) {
        setActive(navServices);
    } else if (scrollPos >= projectsPos && scrollPos < (achievementsPos - halfScr)) {
        setActive(navProjects);
    } else if (scrollPos >= achievementsPos && scrollPos < (contactPos - halfScr)) {
        setActive(navAchievements);
    } else if (scrollPos >= contactPos - halfScr) {
        setActive(navContact);
    }


});
