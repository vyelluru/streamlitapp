{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNOTupF5sFZuaj3aaX2rkkH",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/vyelluru/streamlitapp/blob/main/streamlit_app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kc-UwQvLdUzt",
        "outputId": "76b4fe7b-2d87-4b39-f7ce-b13f968d522c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.25.0-py2.py3-none-any.whl (8.1 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.1/8.1 MB\u001b[0m \u001b[31m15.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting openai\n",
            "  Downloading openai-0.27.8-py3-none-any.whl (73 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m73.6/73.6 kB\u001b[0m \u001b[31m3.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting langchain\n",
            "  Downloading langchain-0.0.254-py3-none-any.whl (1.4 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.4/1.4 MB\u001b[0m \u001b[31m22.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/lib/python3/dist-packages (from streamlit) (1.4)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.3.1)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.6)\n",
            "Requirement already satisfied: importlib-metadata<7,>=1.4 in /usr/lib/python3/dist-packages (from streamlit) (4.6.4)\n",
            "Requirement already satisfied: numpy<2,>=1.19.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.22.4)\n",
            "Requirement already satisfied: packaging<24,>=16.8 in /usr/local/lib/python3.10/dist-packages (from streamlit) (23.1)\n",
            "Requirement already satisfied: pandas<3,>=1.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.5.3)\n",
            "Requirement already satisfied: pillow<10,>=7.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (9.4.0)\n",
            "Requirement already satisfied: protobuf<5,>=3.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.20.3)\n",
            "Requirement already satisfied: pyarrow>=6.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (9.0.0)\n",
            "Collecting pympler<2,>=0.9 (from streamlit)\n",
            "  Downloading Pympler-1.0.1-py3-none-any.whl (164 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m164.8/164.8 kB\u001b[0m \u001b[31m11.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: python-dateutil<3,>=2.7.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.8.2)\n",
            "Requirement already satisfied: requests<3,>=2.18 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.27.1)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.4.2)\n",
            "Requirement already satisfied: tenacity<9,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.2.2)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.7.1)\n",
            "Collecting tzlocal<5,>=1.1 (from streamlit)\n",
            "  Downloading tzlocal-4.3.1-py3-none-any.whl (20 kB)\n",
            "Collecting validators<1,>=0.2 (from streamlit)\n",
            "  Downloading validators-0.20.0.tar.gz (30 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit)\n",
            "  Downloading GitPython-3.1.32-py3-none-any.whl (188 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m188.5/188.5 kB\u001b[0m \u001b[31m13.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting pydeck<1,>=0.8 (from streamlit)\n",
            "  Downloading pydeck-0.8.0-py2.py3-none-any.whl (4.7 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m4.7/4.7 MB\u001b[0m \u001b[31m32.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.1)\n",
            "Collecting watchdog>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-3.0.0-py3-none-manylinux2014_x86_64.whl (82 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m82.1/82.1 kB\u001b[0m \u001b[31m3.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from openai) (4.65.0)\n",
            "Requirement already satisfied: aiohttp in /usr/local/lib/python3.10/dist-packages (from openai) (3.8.5)\n",
            "Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.10/dist-packages (from langchain) (6.0.1)\n",
            "Requirement already satisfied: SQLAlchemy<3,>=1.4 in /usr/local/lib/python3.10/dist-packages (from langchain) (2.0.19)\n",
            "Requirement already satisfied: async-timeout<5.0.0,>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from langchain) (4.0.2)\n",
            "Collecting dataclasses-json<0.6.0,>=0.5.7 (from langchain)\n",
            "  Downloading dataclasses_json-0.5.14-py3-none-any.whl (26 kB)\n",
            "Collecting langsmith<0.1.0,>=0.0.11 (from langchain)\n",
            "  Downloading langsmith-0.0.19-py3-none-any.whl (31 kB)\n",
            "Requirement already satisfied: numexpr<3.0.0,>=2.8.4 in /usr/local/lib/python3.10/dist-packages (from langchain) (2.8.4)\n",
            "Collecting openapi-schema-pydantic<2.0,>=1.2 (from langchain)\n",
            "  Downloading openapi_schema_pydantic-1.2.4-py3-none-any.whl (90 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m90.0/90.0 kB\u001b[0m \u001b[31m7.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: pydantic<2,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain) (1.10.12)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp->openai) (23.1.0)\n",
            "Requirement already satisfied: charset-normalizer<4.0,>=2.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp->openai) (2.0.12)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.10/dist-packages (from aiohttp->openai) (6.0.4)\n",
            "Requirement already satisfied: yarl<2.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp->openai) (1.9.2)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.10/dist-packages (from aiohttp->openai) (1.4.0)\n",
            "Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.10/dist-packages (from aiohttp->openai) (1.3.1)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (3.1.2)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (4.3.3)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
            "Collecting marshmallow<4.0.0,>=3.18.0 (from dataclasses-json<0.6.0,>=0.5.7->langchain)\n",
            "  Downloading marshmallow-3.20.1-py3-none-any.whl (49 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m49.4/49.4 kB\u001b[0m \u001b[31m1.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting typing-inspect<1,>=0.4.0 (from dataclasses-json<0.6.0,>=0.5.7->langchain)\n",
            "  Downloading typing_inspect-0.9.0-py3-none-any.whl (8.8 kB)\n",
            "Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
            "  Downloading gitdb-4.0.10-py3-none-any.whl (62 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.7/62.7 kB\u001b[0m \u001b[31m3.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2022.7.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil<3,>=2.7.3->streamlit) (1.16.0)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.18->streamlit) (1.26.16)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.18->streamlit) (2023.7.22)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.18->streamlit) (3.4)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (2.14.0)\n",
            "Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from SQLAlchemy<3,>=1.4->langchain) (2.0.2)\n",
            "Collecting pytz-deprecation-shim (from tzlocal<5,>=1.1->streamlit)\n",
            "  Downloading pytz_deprecation_shim-0.1.0.post0-py2.py3-none-any.whl (15 kB)\n",
            "Requirement already satisfied: decorator>=3.4.0 in /usr/local/lib/python3.10/dist-packages (from validators<1,>=0.2->streamlit) (4.4.2)\n",
            "Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
            "  Downloading smmap-5.0.0-py3-none-any.whl (24 kB)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
            "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.19.3)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Collecting mypy-extensions>=0.3.0 (from typing-inspect<1,>=0.4.0->dataclasses-json<0.6.0,>=0.5.7->langchain)\n",
            "  Downloading mypy_extensions-1.0.0-py3-none-any.whl (4.7 kB)\n",
            "Collecting tzdata (from pytz-deprecation-shim->tzlocal<5,>=1.1->streamlit)\n",
            "  Downloading tzdata-2023.3-py2.py3-none-any.whl (341 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m341.8/341.8 kB\u001b[0m \u001b[31m16.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hBuilding wheels for collected packages: validators\n",
            "  Building wheel for validators (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for validators: filename=validators-0.20.0-py3-none-any.whl size=19580 sha256=fd8ed56a14a29daef6e08935ad0cae6f7132cf744bce2f0d3218772649c3df0e\n",
            "  Stored in directory: /root/.cache/pip/wheels/f2/ed/dd/d3a556ad245ef9dc570c6bcd2f22886d17b0b408dd3bbb9ac3\n",
            "Successfully built validators\n",
            "Installing collected packages: watchdog, validators, tzdata, smmap, pympler, mypy-extensions, marshmallow, typing-inspect, pytz-deprecation-shim, pydeck, openapi-schema-pydantic, langsmith, gitdb, tzlocal, openai, gitpython, dataclasses-json, streamlit, langchain\n",
            "  Attempting uninstall: tzlocal\n",
            "    Found existing installation: tzlocal 5.0.1\n",
            "    Uninstalling tzlocal-5.0.1:\n",
            "      Successfully uninstalled tzlocal-5.0.1\n",
            "Successfully installed dataclasses-json-0.5.14 gitdb-4.0.10 gitpython-3.1.32 langchain-0.0.254 langsmith-0.0.19 marshmallow-3.20.1 mypy-extensions-1.0.0 openai-0.27.8 openapi-schema-pydantic-1.2.4 pydeck-0.8.0 pympler-1.0.1 pytz-deprecation-shim-0.1.0.post0 smmap-5.0.0 streamlit-1.25.0 typing-inspect-0.9.0 tzdata-2023.3 tzlocal-4.3.1 validators-0.20.0 watchdog-3.0.0\n"
          ]
        }
      ],
      "source": [
        "pip install streamlit openai langchain"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "from langchain.llms import OpenAI"
      ],
      "metadata": {
        "id": "liBhlpa_dafG"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "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\n"
      ],
      "metadata": {
        "id": "I14e3uTmdoJc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "st.title('🦜🔗 Quickstart App')\n",
        "\n",
        "openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')\n",
        "\n",
        "def generate_response(input_text):\n",
        "    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)\n",
        "    st.info(llm(input_text))\n",
        "\n",
        "with st.form('my_form'):\n",
        "    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')\n",
        "    submitted = st.form_submit_button('Submit')\n",
        "    if not openai_api_key.startswith('sk-'):\n",
        "        st.warning('Please enter your OpenAI API key!', icon='⚠')\n",
        "    if submitted and openai_api_key.startswith('sk-'):\n",
        "        generate_response(text)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Etyvlkamdt5g",
        "outputId": "2e07f42e-a7c1-4893-aec5-13106d37d8e7"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2023-08-06 20:08:12.144 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.10/dist-packages/ipykernel_launcher.py [ARGUMENTS]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Kaval3n5duSP"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}