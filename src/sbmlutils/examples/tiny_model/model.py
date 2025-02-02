"""Tiny model example."""
from math import inf

import sbmlutils.layout as layout
from sbmlutils.examples import templates
from sbmlutils.factory import *
from sbmlutils.metadata.sbo import *
from sbmlutils.units import *


mid = "tiny_example"
packages = ["fbc"]
version = 12
notes = Notes(
    [
        """
    <h2>Description</h2>
    <p>A minimal example in <a href="http://sbml.org" target="_blank">SBML</a> format.
    </p>
    <div class="dc:provenance">The content of this model has been carefully created in a manual research effort.</div>
    <div class="dc:publisher">This file has been created by
    <a href="http://sbml.org" title="SBML team" target="_blank">SBML team</a>.</div>

    <h2>Terms of use</h2>
    <div class="dc:rightsHolder">Copyright © 2019 SBML team.</div>
    <div class="dc:license">
        <p>Redistribution and use of any part of this model, with or without modification, are permitted provided
        that the following conditions are met:
        <ol>
          <li>Redistributions of this SBML file must retain the above copyright notice, this list of conditions and
          the following disclaimer.</li>
          <li>Redistributions in a different form must reproduce the above copyright notice, this list of conditions
          and the following disclaimer in the documentation and/or other materials provided
          with the distribution.</li>
        </ol>
        This model is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the
        implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
        </p>
    </div>
    """
    ]
)
creators = templates.creators

# -----------------------------------------------------------------------------
# Units
# -----------------------------------------------------------------------------
model_units = ModelUnits(
    time=UNIT_KIND_SECOND,
    extent="mmole",
    substance="mmole",
    length=UNIT_KIND_METRE,
    area="m2",
    volume=UNIT_KIND_LITRE,
)
units = [
    Unit("m2", [(UNIT_KIND_METRE, 2.0)]),
    Unit("mmole", [(UNIT_KIND_MOLE, 1, -3, 1.0)]),
    Unit("mM", [(UNIT_KIND_MOLE, 1, -3, 1.0), (UNIT_KIND_LITRE, -1.0)]),
    Unit("mmole_per_s", [(UNIT_KIND_MOLE, 1, -3, 1.0), (UNIT_KIND_SECOND, -1.0)]),
]

# -----------------------------------------------------------------------------
# Compartments
# -----------------------------------------------------------------------------
compartments = [
    Compartment(
        sid="c",
        value=1e-5,
        unit=UNIT_KIND_LITRE,
        constant=True,
        name="cell compartment",
        port=True,
    ),
]

# -----------------------------------------------------------------------------
# Species
# -----------------------------------------------------------------------------
species = [
    Species(
        sid="glc",
        compartment="c",
        initialConcentration=5.0,
        substanceUnit="mmole",
        constant=False,
        boundaryCondition=False,
        hasOnlySubstanceUnits=False,
        name="glucose",
        sboTerm=SBO_SIMPLE_CHEMICAL,
        port=True,
    ),
    Species(
        sid="g6p",
        compartment="c",
        initialConcentration=0.1,
        substanceUnit="mmole",
        constant=False,
        boundaryCondition=False,
        hasOnlySubstanceUnits=False,
        name="glucose-6-phosphate",
        sboTerm=SBO_SIMPLE_CHEMICAL,
    ),
    Species(
        sid="atp",
        compartment="c",
        initialConcentration=3.0,
        substanceUnit="mmole",
        constant=False,
        boundaryCondition=False,
        hasOnlySubstanceUnits=False,
        name="ATP",
        sboTerm=SBO_SIMPLE_CHEMICAL,
        port=True,
    ),
    Species(
        sid="adp",
        compartment="c",
        initialConcentration=0.8,
        substanceUnit="mmole",
        constant=False,
        boundaryCondition=False,
        hasOnlySubstanceUnits=False,
        name="ADP",
        sboTerm=SBO_SIMPLE_CHEMICAL,
        port=True,
    ),
    Species(
        sid="phos",
        compartment="c",
        initialConcentration=0,
        substanceUnit="mmole",
        constant=True,
        boundaryCondition=True,
        hasOnlySubstanceUnits=False,
        name="P",
        sboTerm=SBO_SIMPLE_CHEMICAL,
        port=True,
    ),
    Species(
        sid="hydron",
        compartment="c",
        initialConcentration=0,
        substanceUnit="mmole",
        constant=True,
        boundaryCondition=True,
        hasOnlySubstanceUnits=False,
        name="H+",
        sboTerm=SBO_SIMPLE_CHEMICAL,
    ),
    Species(
        sid="h2o",
        compartment="c",
        initialConcentration=0,
        substanceUnit="mmole",
        constant=True,
        boundaryCondition=True,
        hasOnlySubstanceUnits=False,
        name="H2O",
        sboTerm=SBO_SIMPLE_CHEMICAL,
    ),
]

# -----------------------------------------------------------------------------
# Parameters
# -----------------------------------------------------------------------------
parameters = [
    Parameter(
        "Vmax_GK",
        1.0e-6,
        unit="mmole_per_s",
        constant=True,
        sboTerm=SBO_MAXIMAL_VELOCITY,
        name="Vmax Glucokinase",
    ),
    Parameter(
        "Km_glc",
        0.5,
        unit="mM",
        constant=True,
        sboTerm=SBO_MICHAELIS_CONSTANT,
        name="Km glucose",
    ),
    Parameter(
        "Km_atp",
        0.1,
        unit="mM",
        constant=True,
        sboTerm=SBO_MICHAELIS_CONSTANT,
        name="Km ATP",
    ),
    Parameter(
        "Km_adp",
        0.1,
        unit="mM",
        constant=True,
        sboTerm=SBO_MICHAELIS_CONSTANT,
        name="Km ADP",
    ),
    Parameter(
        "Vmax_ATPASE",
        1.0e-6,
        unit="mmole_per_s",
        constant=True,
        sboTerm=SBO_MAXIMAL_VELOCITY,
        name="Vmax ATPase",
    ),
    Parameter(
        sid="zero",
        name="zero bound",
        value=0,
        unit="mmole_per_s",
        constant=True,
        sboTerm=SBO_FLUX_BOUND,
    ),
    Parameter(
        sid="inf",
        name="upper bound",
        value=inf,
        unit="mmole_per_s",
        constant=True,
        sboTerm=SBO_FLUX_BOUND,
    ),
    Parameter(
        sid="minus_1000",
        value=-1000,
        unit="mmole_per_s",
        constant=True,
        sboTerm=SBO_FLUX_BOUND,
    ),
    Parameter(
        sid="plus_1000",
        value=1000,
        unit="mmole_per_s",
        constant=True,
        sboTerm=SBO_FLUX_BOUND,
    ),
]

# -----------------------------------------------------------------------------
# FunctionDefinitions
# -----------------------------------------------------------------------------
functions = [Function(sid="f_oscillation", value="lambda(x, cos(x/10 dimensionless))")]

# -----------------------------------------------------------------------------
# Assignments
# -----------------------------------------------------------------------------
assignments = [InitialAssignment("glc", "4.5 mM")]

# -----------------------------------------------------------------------------
# Rules
# -----------------------------------------------------------------------------
rules = [AssignmentRule("a_sum", "atp + adp", unit="mM", name="ATP + ADP balance")]

# -----------------------------------------------------------------------------
# Reactions
# -----------------------------------------------------------------------------
reactions = [
    Reaction(
        sid="GK",
        name="Glucokinase",
        equation="glc + atp -> g6p + adp + hydron []",
        compartment="c",
        pars=[],
        rules=[],
        formula=("Vmax_GK * (glc/(Km_glc+glc)) * (atp/(Km_atp+atp))", "mmole_per_s"),
        lowerFluxBound="zero",
        upperFluxBound="inf",
        sboTerm=SBO_BIOCHEMICAL_REACTION,
    ),
    Reaction(
        sid="ATPPROD",
        name="ATP production",
        equation="adp + phos + hydron -> atp + h2o []",
        compartment="c",
        pars=[],
        rules=[],
        formula=(
            "Vmax_ATPASE * (adp/(Km_adp+adp)) * f_oscillation(time/ 1 second)",
            "mmole_per_s",
        ),
        lowerFluxBound="zero",
        upperFluxBound="inf",
        sboTerm=SBO_BIOCHEMICAL_REACTION,
    ),
    Reaction(
        sid="EX_glc",
        name="glucose exchange",
        equation="glc -> []",
        compartment="c",
        pars=[],
        rules=[],
        lowerFluxBound="minus_1000",
        upperFluxBound="plus_1000",
        formula=("zero", "mmole_per_s"),
        sboTerm=SBO_EXCHANGE_REACTION,
    ),
    Reaction(
        sid="EX_g6p",
        name="glucose-6 phosphate exchange",
        equation="g6p -> []",
        compartment="c",
        pars=[],
        rules=[],
        lowerFluxBound="minus_1000",
        upperFluxBound="plus_1000",
        formula=("zero", "mmole_per_s"),
        sboTerm=SBO_EXCHANGE_REACTION,
    ),
]

# -----------------------------------------------------------------------------
# Objective function
# -----------------------------------------------------------------------------
objectives = [
    Objective(
        sid="atp_consume_max",
        objectiveType="maximize",
        active=True,
        fluxObjectives={"ATPPROD": 1.0},
    )
]

# -----------------------------------------------------------------------------
# Events
# -----------------------------------------------------------------------------
events = [
    Event(
        "event_1",
        trigger="time >= 200 second",
        assignments={
            "glc": "4.5 mM",
            "atp": "3.0 mM",
            "adp": "0.8 mM",
            "g6p": "0.1 mM",
        },
        name="reset concentrations",
    )
]

# -----------------------------------------------------------------------------
# Constraints
# -----------------------------------------------------------------------------
constraints = [
    Constraint(
        "constraint_1",
        math="atp >= 0 mM",
        message='<body xmlns="http://www.w3.org/1999/xhtml">ATP must be non-negative</body>',
    )
]


# -----------------------------------------------------------------------------
# Layout
# -----------------------------------------------------------------------------
layouts = [
    layout.Layout(
        sid="layout_1",
        name="Layout 1",
        width=700.0,
        height=700.0,
        compartment_glyphs=[
            layout.CompartmentGlyph("glyph_c", compartment="c", x=5, y=5, w=690, h=690)
        ],
        species_glyphs=[
            layout.SpeciesGlyph(
                "glyph_atp", species="atp", x=450, y=50, w=50, h=20, text="ATP"
            ),
            layout.SpeciesGlyph(
                "glyph_adp", species="adp", x=450, y=450, w=50, h=20, text="ADP"
            ),
            layout.SpeciesGlyph(
                "glyph_glc", species="glc", x=50, y=50, w=50, h=20, text="glucose"
            ),
            layout.SpeciesGlyph(
                "glyph_g6p",
                species="g6p",
                x=50,
                y=450,
                w=50,
                h=20,
                text="glucose-6-phosphate",
            ),
            layout.SpeciesGlyph(
                "glyph_hydron",
                species="hydron",
                x=250,
                y=450,
                w=50,
                h=20,
                text="hydron",
            ),
        ],
        reaction_glyphs=[
            layout.ReactionGlyph(
                "glyph_GK",
                reaction="GK",
                x=250 + 25,
                y=250 + 10,
                h=0,
                w=0,
                text="GK",
                species_glyphs={
                    "glyph_atp": layout.LAYOUT_ROLE_SIDESUBSTRATE,
                    "glyph_adp": layout.LAYOUT_ROLE_SIDEPRODUCT,
                    "glyph_glc": layout.LAYOUT_ROLE_SUBSTRATE,
                    "glyph_g6p": layout.LAYOUT_ROLE_PRODUCT,
                    "glyph_hydron": layout.LAYOUT_ROLE_SIDEPRODUCT,
                },
            ),
            layout.ReactionGlyph(
                "glyph_ATPPROD",
                reaction="ATPPROD",
                x=650 + 25,
                y=250 + 10,
                h=0,
                w=0,
                text="ATPase",
                species_glyphs={
                    "glyph_atp": layout.LAYOUT_ROLE_SUBSTRATE,
                    "glyph_adp": layout.LAYOUT_ROLE_PRODUCT,
                },
            ),
        ],
    )
]
