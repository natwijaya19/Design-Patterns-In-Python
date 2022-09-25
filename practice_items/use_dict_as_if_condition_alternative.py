def show_info_about_item(chosen_item="phone"):
    info_dict = {
        "phone": "Handheld communication device",
        "car": "Self-propelled ground vehicle",
        "dinosaur": "Extinct lizard",
        "human": "eat anything",
        "computer": "Electronic device for storing and processing data"

    }

    return info_dict.get(chosen_item, "No info available")


def main():
    print(show_info_about_item())
    print(show_info_about_item("car"))
    print(show_info_about_item("dinosaur"))
    print(show_info_about_item("computer"))
    print(show_info_about_item("human"))


if __name__ == "__main__":
    main()
